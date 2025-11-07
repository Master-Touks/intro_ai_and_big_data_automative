"""
UDS Requirements Effort Estimation Model
=========================================
This script provides a machine learning model to estimate effort hours for
implementing UDS (Unified Diagnostic Services) requirements.

Author: Data Science Team
Date: 2024
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class UDSEffortEstimator:
    """
    A machine learning model to estimate implementation effort for UDS diagnostic requirements.

    This class uses Random Forest Regression to predict effort hours based on various
    features of diagnostic requirements such as session type, service ID, security level, etc.
    """

    def __init__(self):
        """Initialize the estimator with empty model and encoders."""
        self.model = None
        self.encoder_session = LabelEncoder()
        self.encoder_security = LabelEncoder()
        self.encoder_dtc = LabelEncoder()
        self.feature_columns = [
            'Session_Type_encoded',
            'Service_ID_numeric',
            'Sub_function_numeric',
            'Data_Identifier_count',
            'Has_Routine_ID',
            'DTC_Format_encoded',
            'Status_Mask_numeric',
            'Security_Level_encoded',
            'Has_NRC_Code',
            'Response_Time_ms_numeric'
        ]
        self.feature_importance_df = None
        # Store training data for visualization
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.y_pred_train = None
        self.y_pred_test = None

    @staticmethod
    def hex_to_int(value):
        """
        Convert hexadecimal string to integer.

        Args:
            value: String value that may be hex (with '0x' prefix) or '-' for missing

        Returns:
            int: Converted integer value, or 0 if conversion fails
        """
        if value == '-' or pd.isna(value):
            return 0
        try:
            if isinstance(value, str) and value.startswith('0x'):
                return int(value, 16)
            return int(value)
        except:
            return 0

    @staticmethod
    def count_items(value):
        """
        Count comma-separated items in a string.

        Args:
            value: String that may contain comma-separated values

        Returns:
            int: Number of items, or 0 if empty/missing
        """
        if value == '-' or pd.isna(value):
            return 0
        return len(str(value).split(','))

    def prepare_features(self, df, fit_encoders=True):
        """
        Transform raw data into numerical features for the model.

        This method performs the following transformations:
        1. Converts hex values (Service_ID, Sub_function, Status_Mask) to integers
        2. Counts multiple data identifiers
        3. Creates binary features for presence of Routine_ID and NRC_Code
        4. Encodes categorical variables (Session_Type, Security_Level, DTC_Format)
        5. Handles Response_Time with missing values

        Args:
            df: pandas DataFrame with raw requirement data
            fit_encoders: bool, whether to fit encoders (True for training, False for prediction)

        Returns:
            pandas DataFrame with prepared features
        """
        df_prep = df.copy()

        # Convert hexadecimal values to numeric
        print("  Converting hexadecimal values...")
        df_prep['Service_ID_numeric'] = df_prep['Service_ID'].apply(self.hex_to_int)
        df_prep['Sub_function_numeric'] = df_prep['Sub_function'].apply(self.hex_to_int)
        df_prep['Status_Mask_numeric'] = df_prep['Status_Mask'].apply(self.hex_to_int)

        # Count data identifiers (some requirements have multiple)
        print("  Counting data identifiers...")
        df_prep['Data_Identifier_count'] = df_prep['Data_Identifier'].apply(self.count_items)

        # Binary features: presence indicators
        print("  Creating binary features...")
        df_prep['Has_Routine_ID'] = (df_prep['Routine_ID'] != '-').astype(int)
        df_prep['Has_NRC_Code'] = (df_prep['NRC_Code'] != '-').astype(int)

        # Handle Response Time (may have missing values represented as 0 or empty)
        print("  Processing response time...")
        df_prep['Response_Time_ms_numeric'] = pd.to_numeric(df_prep['Response_Time_ms'], errors='coerce').fillna(0)

        # Categorical encodings
        print("  Encoding categorical variables...")
        if fit_encoders:
            df_prep['Session_Type_encoded'] = self.encoder_session.fit_transform(df_prep['Session_Type'])
            df_prep['Security_Level_encoded'] = self.encoder_security.fit_transform(df_prep['Security_Level'])
            df_prep['DTC_Format_encoded'] = self.encoder_dtc.fit_transform(df_prep['DTC_Format'])
        else:
            df_prep['Session_Type_encoded'] = self.encoder_session.transform(df_prep['Session_Type'])
            df_prep['Security_Level_encoded'] = self.encoder_security.transform(df_prep['Security_Level'])
            df_prep['DTC_Format_encoded'] = self.encoder_dtc.transform(df_prep['DTC_Format'])

        return df_prep

    def train(self, df):
        """
        Train the model on historical data.

        Args:
            df: pandas DataFrame with historical requirements data

        Returns:
            tuple: (mae, r2) - Mean Absolute Error and R² score
        """
        print("\n=== Training Model ===")

        # Prepare features
        print("Preparing features...")
        df_prep = self.prepare_features(df, fit_encoders=True)

        # Extract features and target
        X = df_prep[self.feature_columns]
        y = df_prep['Effort_hours']

        print(f"Dataset shape: {X.shape}")
        print(f"Target range: {y.min():.0f} - {y.max():.0f} hours")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=20
        )

        print(f"Training set: {X_train.shape[0]} samples")
        print(f"Test set: {X_test.shape[0]} samples")

        # Create and train model
        print("\nTraining Random Forest model...")
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=20,
            n_jobs=-1
        )

        self.model.fit(X_train, y_train)

        # Evaluate
        print("\nEvaluating model...")
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)

        # save the model

        # Store data for visualization
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.y_pred_train = y_pred_train
        self.y_pred_test = y_pred_test

        mae_train = mean_absolute_error(y_train, y_pred_train)
        mae_test = mean_absolute_error(y_test, y_pred_test)
        r2_train = r2_score(y_train, y_pred_train)
        r2_test = r2_score(y_test, y_pred_test)

        print(f"\n✅ Model trained successfully!")
        print(f"\nTraining Performance:")
        print(f"  Mean Absolute Error: {mae_train:.2f} hours")
        print(f"  R² Score: {r2_train:.3f}")
        print(f"\nTest Performance:")
        print(f"  Mean Absolute Error: {mae_test:.2f} hours")
        print(f"  R² Score: {r2_test:.3f}")

        # Feature importance
        self.feature_importance_df = pd.DataFrame({
            'Feature': self.feature_columns,
            'Importance': self.model.feature_importances_
        }).sort_values('Importance', ascending=False)

        print("\n📊 Top 5 Most Important Features:")
        for idx, row in self.feature_importance_df.head().iterrows():
            print(f"  {row['Feature']}: {row['Importance']:.4f}")

        return mae_test, r2_test

    def predict(self, new_requirement):
        """
        Predict effort for a new requirement.

        Args:
            new_requirement: dict with requirement attributes

        Returns:
            int: Predicted effort in hours (rounded)
        """
        if self.model is None:
            raise ValueError("Model not trained yet! Call train() first.")

        # Convert to DataFrame
        new_df = pd.DataFrame([new_requirement])

        # Prepare features
        new_df_prep = self.prepare_features(new_df, fit_encoders=False)

        # Extract features
        new_X = new_df_prep[self.feature_columns]

        # Predict
        effort = self.model.predict(new_X)[0]

        return round(effort)

    def plot_feature_importance(self, save_path='feature_importance.png'):
        """Plot and save feature importance chart."""
        if self.feature_importance_df is None:
            print("No feature importance data available. Train the model first.")
            return

        plt.figure(figsize=(10, 6))
        plt.barh(self.feature_importance_df['Feature'],
                 self.feature_importance_df['Importance'],
                 color='steelblue')
        plt.xlabel('Importance', fontsize=12)
        plt.ylabel('Feature', fontsize=12)
        plt.title('Feature Importance for Effort Estimation', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n📈 Feature importance plot saved to: {save_path}")
        plt.close()

    def plot_regression_and_residuals(self, save_path='regression_residuals.png'):
        """
        Visualize regression predictions and residual errors.

        This method creates a comprehensive visualization with 4 subplots:
        1. Training set: actual vs predicted values
        2. Test set: actual vs predicted values
        3. Residuals plot: shows the distribution of prediction errors
        4. Residual distribution: histogram of errors

        Args:
            save_path: Path to save the plot (default: 'regression_residuals.png')
        """
        if self.model is None or self.X_train is None:
            print("No training data available. Train the model first.")
            return

        # Calculate residuals
        residuals_train = self.y_train - self.y_pred_train
        residuals_test = self.y_test - self.y_pred_test

        # Create figure with 4 subplots
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

        # Plot 1: Training set - Actual vs Predicted
        ax1 = axes[0, 0]
        ax1.scatter(self.y_train, self.y_pred_train, alpha=0.6, color='steelblue',
                   edgecolors='navy', linewidth=0.5, s=80, label='Predictions')

        # Perfect prediction line
        min_val = min(self.y_train.min(), self.y_pred_train.min())
        max_val = max(self.y_train.max(), self.y_pred_train.max())
        ax1.plot([min_val, max_val], [min_val, max_val],
                'r--', linewidth=2, label='Perfect prediction', alpha=0.7)

        ax1.set_xlabel('Actual Effort (hours)', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Predicted Effort (hours)', fontsize=11, fontweight='bold')
        ax1.set_title('Training Set: Predictions vs Actual', fontsize=12, fontweight='bold')
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)

        # Add R² score
        r2_train = r2_score(self.y_train, self.y_pred_train)
        mae_train = mean_absolute_error(self.y_train, self.y_pred_train)
        ax1.text(0.05, 0.95, f'R² = {r2_train:.3f}\nMAE = {mae_train:.2f}h',
                transform=ax1.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        # Plot 2: Test set - Actual vs Predicted
        ax2 = axes[0, 1]
        ax2.scatter(self.y_test, self.y_pred_test, alpha=0.7, color='coral',
                   edgecolors='darkred', linewidth=0.5, s=100, label='Predictions')

        # Perfect prediction line
        min_val = min(self.y_test.min(), self.y_pred_test.min())
        max_val = max(self.y_test.max(), self.y_pred_test.max())
        ax2.plot([min_val, max_val], [min_val, max_val],
                'r--', linewidth=2, label='Perfect prediction', alpha=0.7)

        ax2.set_xlabel('Actual Effort (hours)', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Predicted Effort (hours)', fontsize=11, fontweight='bold')
        ax2.set_title('Test Set: Predictions vs Actual', fontsize=12, fontweight='bold')
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)

        # Add R² score
        r2_test = r2_score(self.y_test, self.y_pred_test)
        mae_test = mean_absolute_error(self.y_test, self.y_pred_test)
        ax2.text(0.05, 0.95, f'R² = {r2_test:.3f}\nMAE = {mae_test:.2f}h',
                transform=ax2.transAxes, fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        # Plot 3: Residuals plot (errors distribution)
        ax3 = axes[1, 0]
        ax3.scatter(self.y_pred_train, residuals_train, alpha=0.6,
                   color='steelblue', edgecolors='navy', linewidth=0.5, s=80, label='Train')
        ax3.scatter(self.y_pred_test, residuals_test, alpha=0.7,
                   color='coral', edgecolors='darkred', linewidth=0.5, s=100, label='Test')
        ax3.axhline(y=0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Zero error')

        ax3.set_xlabel('Predicted Effort (hours)', fontsize=11, fontweight='bold')
        ax3.set_ylabel('Residuals (Actual - Predicted)', fontsize=11, fontweight='bold')
        ax3.set_title('Residuals Plot: Error Distribution', fontsize=12, fontweight='bold')
        ax3.legend(loc='upper right')
        ax3.grid(True, alpha=0.3)

        # Add standard deviation lines
        std_train = residuals_train.std()
        ax3.axhline(y=std_train, color='steelblue', linestyle=':', linewidth=1.5, alpha=0.5)
        ax3.axhline(y=-std_train, color='steelblue', linestyle=':', linewidth=1.5, alpha=0.5)

        # Plot 4: Distribution of residuals (histogram)
        ax4 = axes[1, 1]

        # Train residuals
        ax4.hist(residuals_train, bins=20, alpha=0.6, color='steelblue',
                edgecolor='navy', label='Train residuals', density=True)

        # Test residuals
        if len(residuals_test) > 0:
            ax4.hist(residuals_test, bins=10, alpha=0.6, color='coral',
                    edgecolor='darkred', label='Test residuals', density=True)

        ax4.axvline(x=0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Zero error')
        ax4.set_xlabel('Residuals (hours)', fontsize=11, fontweight='bold')
        ax4.set_ylabel('Density', fontsize=11, fontweight='bold')
        ax4.set_title('Residual Distribution', fontsize=12, fontweight='bold')
        ax4.legend(loc='upper right')
        ax4.grid(True, alpha=0.3, axis='y')

        # Add statistics
        stats_text = f'Train:\nMean: {residuals_train.mean():.2f}h\nStd: {residuals_train.std():.2f}h'
        if len(residuals_test) > 0:
            stats_text += f'\n\nTest:\nMean: {residuals_test.mean():.2f}h\nStd: {residuals_test.std():.2f}h'
        ax4.text(0.65, 0.95, stats_text, transform=ax4.transAxes,
                fontsize=9, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        # Overall title
        fig.suptitle('Regression Analysis: Model Performance and Residual Errors',
                    fontsize=14, fontweight='bold', y=0.995)

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n📊 Regression and residuals plot saved to: {save_path}")

        # Print interpretation guide
        print("\n" + "=" * 70)
        print("📖 UNDERSTANDING THE PLOTS")
        print("=" * 70)
        print("\n1. PREDICTIONS vs ACTUAL (top plots):")
        print("   - Points closer to the red line = better predictions")
        print("   - R² score closer to 1.0 = model explains variance well")
        print("   - MAE shows average prediction error in hours")

        print("\n2. RESIDUALS PLOT (bottom left):")
        print("   - Points should be randomly scattered around zero")
        print("   - Patterns indicate model bias or missing features")
        print("   - Outliers show cases where model struggles")

        print("\n3. RESIDUAL DISTRIBUTION (bottom right):")
        print("   - Bell curve centered at zero = good model")
        print("   - Skewed distribution = systematic over/under-prediction")
        print("   - Wide distribution = high prediction uncertainty")
        print("=" * 70)

        plt.close()


def main():
    """Main function to demonstrate the usage."""

    print("=" * 70)
    print("UDS REQUIREMENTS EFFORT ESTIMATION MODEL")
    print("=" * 70)

    # Check if CSV file exists
    csv_file = 'uds_requirements_data.csv'
    if not os.path.exists(csv_file):
        print(f"\n❌ Error: CSV file '{csv_file}' not found!")
        print("Please ensure the CSV file is in the same directory as this script.")
        return

    # Load data
    print(f"\n📂 Loading data from {csv_file}...")
    try:
        df = pd.read_csv(csv_file)
        print(f"✅ Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return

    # Display basic info
    print("\n📋 Dataset Overview:")
    print(df.head())
    print("\n📊 Dataset Statistics:")
    print(df.describe())

    # Create and train estimator
    estimator = UDSEffortEstimator()
    mae, r2 = estimator.train(df)

    # Plot feature importance
    estimator.plot_feature_importance()

    # Plot regression analysis and residuals
    estimator.plot_regression_and_residuals()

    # Example predictions
    print("\n" + "=" * 70)
    print("EXAMPLE PREDICTIONS")
    print("=" * 70)

    # Example 1: Extended session with ReadDataByIdentifier
    example1 = {
        'Session_Type': 'Extended',
        'Service_ID': '0x22',
        'Sub_function': '-',
        'Data_Identifier': '0xF190',
        'Routine_ID': '-',
        'DTC_Format': 'ISO15031-6',
        'Status_Mask': '0x08',
        'Security_Level': 'Unlocked',
        'NRC_Code': '-',
        'Response_Time_ms': 40
    }

    effort1 = estimator.predict(example1)
    print(f"\n🔹 Example 1: Extended Session - ReadDataByIdentifier")
    print(f"   Predicted effort: {effort1} hours")

    # Example 2: Programming session with RoutineControl
    example2 = {
        'Session_Type': 'Programming',
        'Service_ID': '0x31',
        'Sub_function': '0x01',
        'Data_Identifier': '-',
        'Routine_ID': '0x0200',
        'DTC_Format': 'ISO15031-6',
        'Status_Mask': '0x00',
        'Security_Level': 'Unlocked',
        'NRC_Code': '0x78',
        'Response_Time_ms': 4750
    }

    effort2 = estimator.predict(example2)
    print(f"\n🔹 Example 2: Programming Session - RoutineControl")
    print(f"   Predicted effort: {effort2} hours")

    # Example 3: Default session with TesterPresent
    example3 = {
        'Session_Type': 'Default',
        'Service_ID': '0x3E',
        'Sub_function': '0x00',
        'Data_Identifier': '-',
        'Routine_ID': '-',
        'DTC_Format': 'ISO15031-6',
        'Status_Mask': '0x00',
        'Security_Level': 'Locked',
        'NRC_Code': '-',
        'Response_Time_ms': 10
    }

    effort3 = estimator.predict(example3)
    print(f"\n🔹 Example 3: Default Session - TesterPresent")
    print(f"   Predicted effort: {effort3} hours")

    print("\n" + "=" * 70)
    print("✅ PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()