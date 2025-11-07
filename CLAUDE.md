General Context

Activity: Software design of engine control units (ECUs) for the French automotive industry (Stellantis Group and Renault).

Team size: 250 people in the department.

Training participants: 8 engineers with no prior knowledge of Big Data or AI.

The training context involves automotive software (ECU development) using embedded C for automation tasks — where topics like LLMs and Copilot could be relevant.
Development includes real-time systems and compilation logs to identify errors (e.g., flashing an ECU on a vehicle).

Other data topics include real-time vehicle data (e.g., analyzing average vehicle age to optimize sales profitability).

A Python/Spark example would be more suitable for the practical exercises.

Prompts

I’d like you to create a 14-hour (2-day) training course based on the program titled
“Programme_Les fondamentaux de l’intelligence artificielle et du big data – 2 jours”,
which is provided as a PDF file.

I’ve included several notes about the company’s context to help you tailor the training.
You also have access to 7 folders in a GCP bucket containing Volvo datasets that can be used to build the practical exercises included in the program.

Please follow the structure of the program to design the 14-hour course, while respecting the constraints described in the notes.md file regarding the company’s context.

The trainees are product engineers who are accustomed to reading code but not writing it.
Since the training focuses on AI and Big Data, I’ve included a notebook example to illustrate the type of simple explanations and demonstrations I’d like to include.

In the notes.md file, you’ll find links to dataset descriptions along with the GCS URIs needed to access them.
The datasets are located in the GCP bucket.

There are also two additional folders:

data_source

riib
Both contain data that can be used as examples during the training.

The training should be designed according to what you’ll read in the file:
“Programme_Les fondamentaux de l’intelligence artificielle et du big data – 2 jours.pdf.”

Finally, I need to write the slides as Markdown (.md) files in a folder named slides, and use the available data (in the GCP bucket, and the folders data_source and riib) to create Python and/or Spark notebooks with practical examples to illustrate the concepts covered in the training.