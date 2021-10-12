  <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/b1H-khJP64gSE3OXQaRuCA" title="7.2. Reading and Writing Files" target="_blank">7.2. Reading and Writing Files</a> </li>
<li><a href="/rltoken/WK3WP_qtPhcDHJo4YNtL5A" title="8.7. Predefined Clean-up Actions" target="_blank">8.7. Predefined Clean-up Actions</a> </li>
<li><a href="/rltoken/8aSPOpBZj9B1DB6GfoEWfg" title="Dive Into Python 3: Chapter 11. Files" target="_blank">Dive Into Python 3: Chapter 11. Files</a> (<em>until &ldquo;11.4 Binary Files&rdquo; (included)</em>)</li>
<li><a href="/rltoken/H2tqUmi9i85WeOjAbRh1Bw" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/derf9VLFVDnSgX2n-drwnw" title="Learn to Program 8 : Reading / Writing Files" target="_blank">Learn to Program 8 : Reading / Writing Files</a> </li>
<li><a href="/rltoken/Y77h8aeRoljlN643yKfdTg" title="Automate the Boring Stuff with Python" target="_blank">Automate the Boring Stuff with Python</a> (<em>ch. 8 p 180-183 and ch. 14 p 326-333</em>)</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/0uedpNilbHerTVsef-PPRQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to open a file</li>
<li>How to write text in a file</li>
<li>How to read the full content of a file </li>
<li>How to read a file line by line</li>
<li>How to move the cursor in a file</li>
<li>How to make sure a file is closed after using it</li>
<li>What is and how to use the <code>with</code> statement</li>
<li>What is <code>JSON</code></li>
<li>What is serialization</li>
<li>What is deserialization</li>
<li>How to convert a Python data structure to a JSON string </li>
<li>How to convert a JSON string to a Python data structure</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

           <h2 class="gap">Tasks</h2>

<h2>0. Read file</h2>
 <p>Write a function that reads a text file (<code>UTF8</code>) and prints it to stdout</p>

<h2>1. Write to a file</h2>
 <p>Write a function that writes a string to a text file (UTF8) and returns the number of characters written</p>

<h2>2. Append to a file</h2>
 Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

<h2>3. To JSON string</h2>
 Write a function that returns the JSON representation of an object (string):

<h2>4. From JSON string to Object</h2>
Write a function that returns an object (Python data structure) represented by a JSON string:

<h2>5. Save Object to a file</h2>
Write a function that writes an Object to a text file, using a JSON representation:

<h2>6. Create object from a JSON file</h2>
Write a function that creates an Object from a “JSON file”:

<h2>7. Load, add, save</h2>
Write a script that adds all arguments to a Python list, and then save them to a file

<h2>8. Class to JSON</h2>
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

<h2>9. Student to JSON</h2>
 <p>Write a class <code>Student</code> that defines a student by:</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>8-class_to_json.py</code>)</li>
<li>You are not allowed to import any module</li>
</ul>

<h2>10. Student to JSON with filter</h2>
Write a class Student that defines a student by: (based on 9-student.py)

<h2>11. Student to disk and reload</h2>
Write a class Student that defines a student by: (based on 10-student.py)

<h2>12. Pascal's Triangle</h2>
