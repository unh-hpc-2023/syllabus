# Syllabus: Introduction to High-Performance Computing

* **Course:** IAM751/851
* **Website:** The class notes etc. will go on the [Course Wiki Page](https://github.com/unh-hpc-2023/syllabus/wiki)
* **Instructor:** Kai Germaschewski, [kai.germaschewski@unh.edu](mailto:kai.germaschewski@unh.edu), Morse 245E
* **Office Hours:** TBD
* **Slack URL** <https://unhhpc2023.slack.com/> (Sign up [here]())
* **Need help?**
  * Ask on [Slack](https://unhhpc2023.slack.com/).
  * Look through and create [issues](https://github.com/unh-hpc-2023/syllabus/issues).
  * [Email](mailto:kai.germaschewski@unh.edu) me for 1-on-1 help, or to
     set up a time to meet.

## Course Summary

Topics include: Elementary Numerical
Methods, Algorithm Development and Optimization, Parallel Programming
Techniques, Distributed Processing over Multiple CPUs, Code Management
and Interfacing to Fortran/C Programming Libraries, Data
Visualization, Source Control.

## Course Description

This course gives an introduction into various areas of
high-performance computing, providing a basis for writing and working
with high-performance simulation codes.

The three main focus areas are "barely sufficient software
engineering", basics of high-performance and parallel programming, and
visualization. Special topics may include a modern HPC language like
[Julia](http://julialang.org), specific hardware architectures,
automatic code generation and performance tuning, or maybe some
machine learning.

The section on software engineering will introduce basic tools and
methods for writing and maintaining portable code, selecting the right
language for a task at hand, and exploiting existing tools.

In the section on high-performance computing, we will review the
history of HPC, future directions and how it is now necessary to use
parallelism at multiple levels. Basic parallel programming models will
be introduced, with a focus on learning how to use MPI.

The last section will provide an overview of some of the visualization
packages available, with a focus on getting to know python/matplotlib
and Visit. Other topics are possible, like GPUs or data science /
machine learning.

## Prerequisites

Enrollment in a CEPS graduate program, MATH 753,
working knowledge of a programming language (C, C++ or Fortran), or by
permission of instructor.

## Reading

There is no required textbook for this class. Occasional readings assignments
will be posted and particpants are expected to finish those before
class time.

Here are some books that might be useful:

* Writing Scientific Software -- A guide to good style, by Suely
   Oliveira \& David Stewart, Cambridge, 2006

* Parallel Programming, by Barry Wilkinson and Michael Allen, Pearson
   Prentice Hall, 2005

* Parallel Programming in C with MPI and OpenMP, by Michael J. Quinn,
   Michelle L. Flomenhoft, Elizabeth, A. Jones, McGraw-Hill, 2003

* Additional Resources:

  * [CMake documentation](https://cmake.org/documentation/)

  * [GNU Autoconf, Automake and Libtool](http://sources.redhat.com/autobook/)

  * [Barely sufficient software engineering](http://www.cs.sandia.gov/~maherou/docs/BarelySufficientSoftwareEngineering.pdf)

  * [Mercurial: The Definitive Guide by Bryan O'Sullivan](http://hgbook.red-bean.com/)

  * [Version control with Subversion](http://svnbook.red-bean.com/)

  * [Numpy and Scipy Documentation](http://sources.redhat.com/autobook/)

  * [PETSc Documentation](http://www.mcs.anl.gov/petsc/petsc-as/documentation/index.html)

  * [VisIt Documentation](https://wci.llnl.gov/codes/visit/manuals.htm)

  * [HDF5 Documentation](http://www.hdfgroup.org/HDF5/doc/doc-info.html)

## Grading Policy

Regular homework and reading [assignments](https://github.com/unh-hpc-2023/syllabus/wiki/Assignments) will be given and
are expected to be completed by their due date. Late submissions may
receive partial credit, but no credit is given after sample solutions
are posted. Attendance and participation in class discussions and in-class exercises
is required. Homework will be posted on the respective class web
pages; it is your responsibility to check for new assignments.

In addition there will be two projects: one midterm project and one
final project. Some projects may be divided into a number of
subprojects which are expected to be finished by their individual due
date, before the due date of the complete project. Some of the
assignments will be designated as team efforts.

Every student is expected to give one presentation to the rest of the
class during the course of the semester. You will research one
specific topic (from the area of HPC) and introduce it to the rest of
the class. Ideally, you will pick your topic yourself according to
your interests, in coordination with the instructor.

The final grade will be calculated as follows: Homework assignments
and class participation 30%, presentation 10%, midterm project: 30%, final project: 30%

## Accessibility Services

According to the Americans with Disabilities Act (as amended, 2008),
 each student with a disability has the right to request services from
 UNH to accommodate his/her disability. If you are a student with a
 documented disability or believe you may have a disability that
 requires accommodations, please contact Student Accessibility
 Services (SAS) at 201 Smith Hall. Accommodation letters are created
 by SAS with the student. Please follow-up with your instructor as
 soon as possible to ensure timely implementation of the identified
 accommodations in the letter. Faculty have an obligation to respond
 once they receive official notice of accommodations from SAS, but are
 under no obligation to provide retroactive accommodations.

## Emotional or Mental Health Distress

Your academic success and overall mental health is very important.
If, during the semester, you find you are experiencing emotional or
mental health issues, please contact the [University’s Psychological
and Counseling Services  (PACS)](https://www.unh.edu/pacs/) (3rd floor, Smith Hall;
603-862-2090/TTY:  7-1-1) which provides counseling appointments and
other mental health services.   If urgent, students may call PACS M-F,
8 a.m.-5 p.m., and schedule an Urgent Same-Day Appointment.

## Students of All Faiths

In the event that a student needs accommodation for a religious or cultural holiday/observance,
that student is encouraged to make that request as early in the semester as possible.

## Confidentiality and Mandatory Reporting

   The University of New Hampshire and its faculty are committed to
   assuring a safe and productive educational environment for all
   students and for the university as a whole.   To this end, the
   university requires faculty members to report to the university’s
   Title IX Coordinator (Donna Marie Sorrentino, dms@unh.edu,
   603-862-2930/1527 TTY) any incidents of sexual violence and
   harassment shared by students.

   If you wish to speak to a confidential support service provider who
   does not have this reporting responsibility because their
   discussions with clients are subject to legal privilege, you can
   find a list of resources
   here
   [(privileged confidential service providers/resources)](https://www.unh.edu/affirmativeaction/offices-resources-support).
   For more information about what happens when you report, how the
   university considers your requests for confidentiality once a
   report is made to the Title IX Coordinator, your rights and report
   options at UNH (including anonymous report options) please
   visit [(student reporting options)](https://www.unh.edu/affirmativeaction/reporting-students).

## Health and Safety

Faculty, TAs, and course instructors are critical partners in promoting our #unhtogether COVID
response culture. We all have a responsibility during this COVID-19 pandemic to protect our
own health and the health of friends and fellow community members. Violations of the COVID
protocols by even a single individual can cause significant disruptions or discontinuation of inperson academic activities. Any student creating such disruptions undermines the opportunity for
others to learn and engage with the UNH community, and as such, is in serious violation of the
UNH Student Rights, Rules, & Responsibilities.

All students are required to wear masks in class and in any other indoor spaces where people
will be close to one another for more than a few minutes, unless a medical exception is made
through an accommodation process. It is your responsibility to obtain a mask before coming
to class. For information on proper use of masks, acceptable mask types, and other PPE and
social distancing guidelines visit (<https://www.unh.edu/coronavirus>). Students wishing to
request a medical accommodation should contact the Student Accessibility Services (link).
Failure to comply with PPE or any other UNH COVID protocols is a violation of the Student
Rights, Rules, and Responsibilities. If you refuse to comply, you will be asked to leave class
immediately and you may also be reported to the Office of the Dean of Students and your
associate dean.

<!-- ## Modality

This class is beginning the semester operating
in face-to-face operations with a mask requirement in place. If your health and safety require
shifting to additional precautions such as social distancing, the modality and schedule of this
course may change.

I will log onto Zoom during class time (see Canvas), so that students who cannot be in class at any given day can follow remotely. I will record these zoom sessions and make them available on request. -->
