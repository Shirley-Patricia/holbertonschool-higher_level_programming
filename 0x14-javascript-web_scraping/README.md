<h1>0x14. JavaScript - Web scraping</h1>
<h2>Tasks</h2>
<h2>0.Readme</h2>
<p>Write a script that reads and prints the content of a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>

<h2>1.Write me</h2>
<p>Write a script that writes a string to a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>

<h2>2.Status code</h2>

<p>Write a script that display the status code of a <code>GET</code> request.</p>

 <ul>
 <li>The first argument is the URL to request (<code>GET</code>)</li>
 <li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
 <li>You must use the module <code>request</code></li>
 </ul>
 
<h2>3.Star wars movie title</h2>
<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>

<ul>
<li>The first argument is the movie ID</li>
<li>You must use the <a href="/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q" title="Star wars API" target="_blank">Star wars API</a> with the endpoint <code>https://swapi-api.hbtn.io/api/films/:id</code></li>
<li>You must use the module <code>request</code></li>
</ul>

<h2>4.Star wars Wedge Antilles</h2>

<p>Write a script that prints the number of movies where the character &ldquo;Wedge Antilles&rdquo; is present.</p>

<ul>
<li>The first argument is the API URL of the <a href="/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q" title="Star wars API" target="_blank">Star wars API</a>: <code>https://swapi-api.hbtn.io/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code> - your script <strong>must</strong> use this ID for filtering the result of the API</li>
<li>You must use the module <code>request</code></li>
</ul>
