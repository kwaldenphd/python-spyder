# Python in Spyder

<a href="http://creativecommons.org/licenses/by-nc/4.0/" rel="license"><img style="border-width: 0;" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" alt="Creative Commons License" /></a>
This tutorial is licensed under a <a href="http://creativecommons.org/licenses/by-nc/4.0/" rel="license">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

## Lab Goals

This lab covers installing Anaconda and getting started in the Spyder IDE. The lab also covers stepwise debugging and the `log()` function.

By the end of this lab, students will be able to:
- Install Spyder in their local environment
- Understand the core components of the Spyder IDE
- Understand the conceptual elements of step-wise debugging
- Understand how to use step-wise debugging in the Spyder IDE

## Acknowledgements

Peer review and editing was provided by Spring 2021 graduate teaching assistants [Subhadyuti Sahoo](https://github.com/SDSAHOO703) and [Aidan Draper](https://github.com/adraper2).

Information and exercises in this lab are adapted from the following texts:
- Al Sweigart's [*Automate the Boring Stuff With Python*](https://nostarch.com/automatestuff2) (No Starch Press, 2020).
  * Chapter 11, "Debugging" (249-266)

The author consulted the following texts when writing this tutorial:
- Allen Downey, [*Think Python: How to Think Like a Computer Scientist*](https://www.oreilly.com/library/view/think-python-2nd/9781491939406/) (O'Reilly, 2015).
  * Chapter 2 "Variables, Expressions and Statements" (11-20)
- Quinn Dombrowski, Tassie Gniady, and David Kloster, "Introduction to Jupyter Notebooks," *The Programming Historian* 8 (2019), https://doi.org/10.46430/phen0087

# Table of Contents

- [Lab notebook templates](#lab-notebook-templates)
- [Different types of Python environments](#different-types-of-python-environments)
- [Installing Anaconda](#installing-anaconda)
- [Python in Spyder](#python-in-spyder)
  * [Installing packages in Spyder](#installing-packages-in-spyder)
- [Debugging](#debugging)
  * [Stepwise debugging in Spyder](#stepwise-debugging-in-spyder)
  * [Other approaches to debugging](#other-approaches-to-debugging)
  * [But why can't I debug using `print()`](#but-why-cant-i-debug-using-print)
- [Python refresh](#python-refresh)
- [Lab notebook questions](#lab-notebook-questions)

[Link to lab procedure as a Jupyter Notebook](https://colab.research.google.com/drive/10QmGPFhFGm84IEozY60fzySftcdTPV3m?usp=sharing)

# Lab notebook templates

[Google Doc template for Q1-Q7](https://docs.google.com/document/d/1uzSvhUaZngfGB9t-HCLK3YWNfMbyNPL9plQyh4Jm4zg/copy)

[`.py` template for Q1-Q8](https://drive.google.com/file/d/1uE_2ue3CydJYOPLLtKZLz0zY37MLGSnT/view?usp=sharing)

[`.py` template for just Q8](https://drive.google.com/file/d/1UvqINgtcJL1-UHX6pT0KlvxjSGiKySzT/view?usp=sharing)

[Jupyter Notebook (`.ipynb`) template for Q1-Q8](https://colab.research.google.com/drive/1oLcEdU1z4TfGaspRfDh_r4tRTQ5bwW6r?usp=sharing)

# Different types of Python environments

1. Up to this point, we have used the browser-based IDE [Replit](https://repl.it/).

2. What is an IDE? "An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger" ([Wikipedia](https://en.wikipedia.org/wiki/Integrated_development_environment)).

3. An IDE can include features like syntax highlighting, code completion, version control, and debugging.

5. There are a WIDE range of IDEs that are proprietary or open-source, tailored to a specific language or able to work across languages.

5. Some common IDEs include Eclipse, Geany, Brackets, Atom, PyCharm, Spyder, RStudio, etc. For more in IDEs, visit Wikipedia's ["Comparison of integrated development environments"](https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments) page.

6. Replit (generally) worked for (most of) our needs. But it ran into problems with more complex programs or programs involving external files/datasets/etc. 

7. Now, we're going to install Python on your local computer, using a distribution called Anaconda.

8. What is Anaconda? "Anaconda is a open-source distribution of the Python and R programming languages for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS. It is developed and maintained by Anaconda, Inc., which was founded by Peter Wang and Travis Oliphant in 2012" ([Wikipedia](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))).

9. The Anaconda environment includes a number of specific tools and programs, including:
- JupyterLab
- Jupyter Notebook
- Qt Console
- Spyder
- Glue
- Orange
- RStudio
- Visual Code Studio

10. In this lab, we'll be focusing on the Spyder IDE.

# Installing Anaconda

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_1.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_1.png?raw=true" /></a></p>

Windows/PC instructions:
- Anaconda Documentation, ["Installing on Windows"](https://docs.anaconda.com/anaconda/install/windows/) *Anaconda* (2020).
- ProgrammingKnowledge, ["Install Anaconda Python, Jupyter Notebook and Spyder on Windows 10"](https://youtu.be/5mDYijMfSzs) *YouTube video* (4 September 2018).

Mac OS instructions:
- Anaconda Documentation, ["Installing on macOS"](https://docs.anaconda.com/anaconda/install/mac-os/) *Anaconda* (2020).
- Understanding Data, ["Easily Install Anaconda Python Distribution On Mac OS X"](https://youtu.be/V6ZAv7hBH6Y) *YouTube video* (16 October 2019).

Chromebook instructions:
- Alex P. Miller, ["Data Science on a Chromebook: How to run Jupyter, Python, and R locally in ChromeOS"](https://alex.miller.im/posts/data-science-chromebook-pixelbook-jupyter-python-r/) *personal blog* (6 March 2019).
- Noebrian, ["Installing Anaconda on a Chromebook"](https://chromebook.home.blog/2019/01/20/installing-anaconda-on-a-chromebook-no-dev-beta-or-crouton-needed/) *ChromeBooks* (20 January 2019).

To install Spyder as a stand-alone program: https://www.spyder-ide.org/

# Python in Spyder

11. What is Spyder? 

12. "Spyder is a free and open source scientific environment written in Python, for Python, and designed by and for scientists, engineers and data analysts. It features a unique combination of the advanced editing, analysis, debugging, and profiling functionality of a comprehensive development tool with the data exploration, interactive execution, deep inspection, and beautiful visualization capabilities of a scientific package" ([Spyder documentation](https://www.spyder-ide.org/)).

13. Spyder's core components include:
- Editor
- IPython console
- Variable explorer
- Plots
- Debugger
- Help

14. These robust Python features in Spyder will be incredibly useful as we start to do more work with datasets, visualizations (plots), and debugging in more complex programming environments.

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_1.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_1.png?raw=true" /></a></p>

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2.png?raw=true" /></a></p>

15. Open the Anaconda navigator and select the option to launch Spyder.

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2a.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2a.png?raw=true" /></a></p>

16. Spyder has three default panes that show up when you launch the program.

17. Your `.py` file shows up on the left-hand side of the program window. 

18. This is where you will write Python code. 

19. You can have multiple `.py` files open in Spyder and navigate between the tabs. 

20. The top-right pane has four default options:
- Variable explorer, which lets you see named variables in your program
- Help, which provides additional documentation, information, or resources
- Plots, which will show visualizations generated by your program
- Files, which will show all files currently open or active in your Spyder workspace

21. The bottom-right pane is the Console, which lets you execute and test Python commands. You can have multiple consoles open simultaneously.

22. So how is the Console different from your `.py` file?

23. In the `.py` file you are writing a Python program that will run or execute when the file is called. You make updates to that file, save changes, etc.

24. The Console lets you execute Python commands but is not saving those commands as part of a `.py` file. 

25. Great for testing. Less great for building out complex programs.

26. NOTE: When we were working in Replit, all files that were part of our Python project were in the same virtual workspace. 

27. That's not going to be the case when working in a desktop IDE like Spyder. 

28. Think of this as the difference between working with files in Google Drive versus on your local computer. 

29. You can set a working directory, which is where Spyder will look for external files you are wanting to access from within a Python program. The working directory is also where Python will save `.py` files you build.

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2c.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_2c.png?raw=true" /></a></p>

30. Click on the folder icon in the top-right hand corner of Spyder (next to the arrow icon) to set a working directory. It doe--where you save `.py` files and other files (think data files) you might be wanting to access as part of a Python program.

31. Now, files don't have to be in your current working directory for you to access them in Python. But you'll need to provide the full file path (i.e. location information or directory information for where that file is located on your computer).

32. Go ahead and create an `EoC_II` folder and set that folder as your working directory in Spyder. 

33. It might also be a good idea to start creating lab-specific sub-folders within your `EoC_II` parent folder. 

34. This will help with organization as we move through labs and work with a variety of sample files and datasets.

<blockquote>Q1: Work through the <a href="https://docs.spyder-ide.org/current/videos/first-steps-with-spyder.html">"First Steps with Spyder"</a>resources provided in the Spyder documentation. That includes two 3.5 minute videos that introduce you to the basics of the Spyder IDE and how to get started with Python in Spyder. Describe your experience getting  started with Spyder using  these materials/resources.</blockquote>

<blockquote>Q2: How is Spyder different than previous IDEs? What do you see as strengths/advantages? What do you see as possible challenges?</blockquote>

<blockquote>OPTIONAL: Take a <code>.py</code> lab notebook file and load it into Spyder. Explore how the program runs in a different IDE. In particular, explore Spyder's options to run portions or a selection of the larger program. How does this change the way you interact with the program?</blockquote>

## Installing packages in Spyder

35. From the Anaconda navigator, you can select the option to launch a terminal.

36. In that terminal, you can use `pip install package-name` to install any needed packages.

37. You can check what packages are installed using the terminal or the GUI "Environments" option.

38. You can also let Anaconda manage your packages with the conda package manager.

39. Most packages will have an alternate install syntax for conda that starts with `conda install package-name`.

40. NOTE: Installing packages using `conda` only installs the package in the Anaconda environment. `pip` installs the package in any environment.

41. For more on the conda package manager: 
- [Anaconda Documentation, Installing conda packages](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)
- Jake VanderPlas, ["Conda: Myths and Misconceptions"](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/) *Pythonic Perambulations personal blog* (25 August 2016)

# Debugging

42. To paraphrase an old programming joke, writing code is 90% of the work of programming. Debugging is the other 90%.

43. You've been working on a program for hours, your head hurts, and something still isn't working. We all know a version of that feeling.

44. There's no easy solution that will prevent all problems (or "bugs") in your code. But having strategies for testing your code, recognizing and making sense of error messages, and methodically debugging your code can help immensely.

45. Python errors will usually fall into three types: syntax, runtime, and semantic.

46. Syntax refers to the structure of a program and rules about that structure. 

47. ***Syntax errors*** involve things like indentation, parenthesis, etc. The Python interpreter expects the language to be structured a specific way, and throws a syntax error when it's not.

48. ***Runtime errors***, or ***exceptions***: appears after a program has started running. These errors indicate something unexpected has happened that interrupts or stops the program execution. 

49. Things that can cause a runtime error include:
- Misspelled or incorrectly capitalized variables or function names
- Dividing by zero
- Mismatched data types (i.e. attempting to perform operations on data of the wrong type)
- Attempting to use a type conversion function on a value that can't be converted

50. Semantic: relates to meaning. 

51. ***Semantic errors*** have to do with the meaning (or purpose/intent) of your code. Semantic errors don't show up as error messages-but the program will not do what you expect it to do. 

52. The debugging strategies discussed here will focus on semantic errors but are useful for all types of errors.

## Stepwise debugging in Spyder

53. Spyder will catch many syntax and runtime errors. 

54. Hover over a red `X` by any of your lines of code to see more information about a possible error.

55. Spyder integrates the enhanced `ipdb` debugger, which gives you robust options for troubleshooting or debugging your code.

56. Specifically, the debugger will let you run a program line by line, running a single line of code and waiting for you to tell it to continue.

57. Running your program through this kind of debugging is immensely valuable for tracking down bugs or catching complex issues in a program.

58. This mode of debugging includes the following possible steps or "moves":
- Continue (run the program until the next breakpoint)
- Step in (executes the next line of code; if the next line of code is a function, the debugger will 'step into' the first line of that function)
- Step over (executes the next line of code, but will not go line-by-line through the function; the debugger 'steps over' the function code and waits for the function call to return)
- Step out (lets you step out of a function if you used step in and want to 'step out' of the function)
- Stop (stops debugging and terminates the program)

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_3.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_3.png?raw=true" /></a></p>

<p align="center"><a href="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_4.png?raw=true"><img class="aligncenter" src="https://github.com/kwaldenphd/python-spyder/blob/main/images/Figure_4.png?raw=true" /></a></p>

59. Let's use this approach and Spyder functionality to debug a number adding program.

```Python
print('Enter the first number to add: ')
first = input()
print('Enter the second number to add: ')
second = input()
print('Enter the third number to add: ')
third = input()
print('The sum is ' + first + second + third)
```

60. First run the program without the debugger enabled. What happens?

61. Debug the file going line-by-line. Remember to use `Step Over` to execute functions without going into each line of the function code.
- Functions in this sample program include `print()` and `input()`
- You can always `Step Out` if you accidently step into a function

<blockquote>Q3: What type of error does this program return (syntax, runtime, semantic) and why? How would we go about modifying the program to address this error?</blockquote>

## Other approaches to debugging

62. If you've never put a `print()` statement in your code to output a variable's value while the program is running, you have used a form of `logging` to debug your code.

63. Python's `logging` module lets you record custom messages that output as part of your program. 

64. These `log` messages describe when the program reaches a point where a logging function is called and what variables have been specified at that point.

65. Step one is to import the `logging` module and set up basic configuration for the module at the top of your `.py` file.
```Python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

66. This configuration information instructs Python to create a `LogRecord` object when a logging function is called, and to include specific information about that event in the `LogRecord` object.

67. So how would we use the `logging` module when writing a program?

68. Say we were creating a function that calcualted the factorial of a given number.
- Factorial 4 is 1 x 2 x 3 x 4 = 24
- Factorial 7 is 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040

```Python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s%%)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s%%)' % (n))
  return total

print(factorial(5))
logging.debug('End of program')
```

69. Anytime we call the `logging.debug()` function, the configuration information from the start of the file governs the log formatting and messages.

<blockquote>Q4: What happens when we run this program? What kinds of log messages do we get, and what information do they give us?</blockquote>

<blockquote>Q5: Is this program doing what we expect? Where would you go next with debugging or addressing the error?</blockquote>

## But why can't I debug using `print()`

70. It can seem unwieldy to configure the `logging` module and write lines of code dedicated just to logging what's happening in your program.

71. But think about the factorial example. Log messages led us right to the program's issue. 

72. Trying to debug using `print()` calls means you'll have to go back through each line of your program to remove `print()` statements used for debugging (while also making sure you aren't removing `print()` statements that are a component of the actual program).

73. Think of the `logging` module as a report that generates alongside your program output as it executes. The program executes and you also have useful log information about what happened along the way.

74. Once you're done debugging the program, you can add the `logging.disable()` function to the start of your program to supress the log messages without actually having to modify your program.

<blockquote>Visit Python's <a href="https://docs.python.org/3/howto/logging.html">Logging HOWTO</a> documentation to learn more about the logging module.</blockquote>

<blockquote>Q6: What are your thoughts on this approach to identifying what's happening in your program? What seems appealing? What seems challenging? When or how could this approach be useful?</blockquote>

<blockquote>Q7: Compare your experience working in different Python IDEs. What seems appealing about each? What seems challenging? Based on this experience, what is your preference, or are there situations in which you'd prefer one over the other?</blockquote>

# Python Refresh

75. The last thing we'll do in this lab is make sure you're comfortable with a few core elements of Python syntax. 

76. For each component, you're asked to describe the concept in your own words and write an example of the concept using Python syntax.

77. Reusing programs you wrote for Elements I labs is absolutely fine. Consulting Elements I lab procedures/documentation is also fine.

77. You can submit this portion of the lab as a `.py` or `.ipynb` file- whatever is easiest. But I encourage folks to use these tasks as an opportunity to get more familiar/comfortable with Spyder.

<blockquote>Q8: For each concept, describe in your own words and provide an example using Python syntax. Use comments/narrative text to note each part of your answer.
<ol type="a">
<li><a href="https://github.com/kwaldenphd/python-intro#your-first-program"><code>print</code>statement</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#variables-and-types">string variable</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#variables-and-types">integer variable</a></li>
<li><a href="https://github.com/kwaldenphd/python-lists-strings#concatenation">concatenation</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#operators">arithmetic operators</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#operators">comparison operators</a></li>
<li><a href="https://github.com/kwaldenphd/python-lists-strings">list</a></li>
<li><a href="https://github.com/kwaldenphd/python-dictionaries-sets#dictionaries">dictionary</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>if, else, elif</code> statements</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>for</code> loop</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>while</code> loop</a></li>
<li><a href="https://github.com/kwaldenphd/python-functions">functions</a></li>
<li><a href="https://github.com/kwaldenphd/pandas-intro">Pandas <code>dataframe</code></a></li>
</ol>
</blockquote>

# Lab notebook questions

Lab notebook templates:
- [Google Doc template for Q1-Q7](https://docs.google.com/document/d/1uzSvhUaZngfGB9t-HCLK3YWNfMbyNPL9plQyh4Jm4zg/copy)
- [`.py` template for Q1-Q8](https://drive.google.com/file/d/1uE_2ue3CydJYOPLLtKZLz0zY37MLGSnT/view?usp=sharing)
- [`.py` template for just Q8](https://drive.google.com/file/d/1UvqINgtcJL1-UHX6pT0KlvxjSGiKySzT/view?usp=sharing)
- [Jupyter Notebook (`.ipynb`) template for Q1-Q8](https://colab.research.google.com/drive/1oLcEdU1z4TfGaspRfDh_r4tRTQ5bwW6r?usp=sharing)

Q1: Work through the <a href="https://docs.spyder-ide.org/current/videos/first-steps-with-spyder.html">"First Steps with Spyder"</a>resources provided in the Spyder documentation. That includes two 3.5 minute videos that introduce you to the basics of the Spyder IDE and how to get started with Python in Spyder. Describe your experience getting  started with Spyder using  these materials/resources.

Q2: How is Spyder different than previous IDEs? What do you see as strengths/advantages? What do you see as possible challenges?

Q3: What type of error does this program return (syntax, runtime, semantic) and why? How would we go about modifying the program to address this error?

```Python
print('Enter the first number to add: ')
first = input()
print('Enter the second number to add: ')
second = input()
print('Enter the third number to add: ')
third = input()
print('The sum is ' + first + second + third)
```

Q4: What happens when we run this program? What kinds of log messages do we get, and what information do they give us?

```Python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
  logging.debug('Start of factorial(%s%%)' % (n))
  total = 1
  for i in range(n + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(%s%%)' % (n))
  return total

print(factorial(5))
logging.debug('End of program')
```

Q5: Is this program doing what we expect? Where would you go next with debugging or addressing the error?

Q6: What are your thoughts on this approach to identifying what's happening in your program? What seems appealing? What seems challenging? When or how could this approach be useful?

Q7: Compare your experience working in different Python IDEs. What seems appealing about each? What seems challenging? Based on this experience, what is your preference, or are there situations in which you'd prefer one over the other?

Q8: For each concept, describe in your own words and provide an example using Python syntax. Use comments/narrative text to note each part of your answer.
<ol type="a">
<li><a href="https://github.com/kwaldenphd/python-intro#your-first-program"><code>print</code>statement</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#variables-and-types">string variable</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#variables-and-types">integer variable</a></li>
<li><a href="https://github.com/kwaldenphd/python-lists-strings#concatenation">concatenation</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#operators">arithmetic operators</a></li>
<li><a href="https://github.com/kwaldenphd/python-intro#operators">comparison operators</a></li>
<li><a href="https://github.com/kwaldenphd/python-lists-strings">list</a></li>
<li><a href="https://github.com/kwaldenphd/python-dictionaries-sets#dictionaries">dictionary</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>if, else, elif</code> statements</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>for</code> loop</a></li>
<li><a href="https://github.com/kwaldenphd/python-conditional-statements#table-of-contents"><code>while</code> loop</a></li>
<li><a href="https://github.com/kwaldenphd/python-functions">functions</a></li>
<li><a href="https://github.com/kwaldenphd/pandas-intro">Pandas <code>dataframe</code></a></li>
</ol>
