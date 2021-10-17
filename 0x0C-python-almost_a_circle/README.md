  <h2>Background Context</h2>

<p>The AirBnB project is a big part of the Higher level curriculum. 
This project will help you be ready for it.</p>

<p>In this project, you will review everything about Python:</p>

<ul>
<li>Import</li>
<li>Exceptions</li>
<li>Class</li>
<li>Private attribute</li>
<li>Getter/Setter</li>
<li>Class method</li>
<li>Static method</li>
<li>Inheritance</li>
<li>Unittest</li>
<li>Read/Write file</li>
</ul>

<p>You will also learn about:</p>

<ul>
<li><code>args</code> and <code>kwargs</code></li>
<li>Serialization/Deserialization</li>
<li>JSON</li>
</ul>

<video autoplay  loop >
  <source type="video/mp4" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4"></source>
</video>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/LroIjBBI5Gqq3ciR-OHmxg" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/TY4rfu2AZtXlRmPVNZm1Lw" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/T7uxwxtGdbRRW9pkD4eO0g" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/SfEo3RQeAXXYI9yabFRw3g" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/4pcL_NcWIg6st6SJ_LN8HQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h3>Tasks</h3>

0. If it&#39;s not tested it doesn&#39;t work
	All your files, classes and methods must be unit tested and be PEP 8 validated.

1. Base class

 <p>Write the first class <code>Base</code>:</p>

<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python package</p>

<p>Create a file named <code>models/base.py</code>:</p>

<ul>
<li>Class <code>Base</code>:

<ul>
<li>private class attribute <code>__nb_objects = 0</code></li>
<li>class constructor: <code>def __init__(self, id=None):</code>:

<ul>
<li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> with this argument value - you can assume <code>id</code> is an integer and you don&rsquo;t need to test the type of it</li>
<li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
</ul></li>
</ul></li>
</ul>

<p>This class will be the &ldquo;base&rdquo; of all other classes in this project. The goal of it is to manage <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</p>

2. Write the class Rectangle that inherits from Base
3. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
4.  <p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>

5. <p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don&rsquo;t need to handle <code>x</code> and <code>y</code> here.</p>

6. <p>Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code></p>

7. <p>Update the class <code>Rectangle</code> by improving the public method <code>def display(self):</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code></p>

8. <p>Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args):</code> that assigns an argument to each attribute:</p>

9. <p>Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args):</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributes:</p>

