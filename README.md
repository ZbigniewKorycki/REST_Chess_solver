<h1>REST Chess solver</h1>

This Flask-based API provides endpoints to retrieve available moves for chess figures and validate chess moves.

<h2>Getting Started</h2>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h3>Prerequisites</h3>

Make sure you have Python installed. This project uses Python 3.8.0

<h3>Installing</h3>

Clone the repository:

```bash
git clone https://github.com/ZbigniewKorycki/REST_Chess_solver.git
cd REST_Chess_solver
```

Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

<h3>Running the Application</h3>

To start the server, run:

```bash
python app.py
```

<h3>Endpoints</h3>

Get List of Available Moves
<ul>
  <li><b>URL: '/api/v1/&lt;chess_figure&gt;/&lt;current_field&gt;'</b></li>
  <li><b>Method: 'GET'</b></li>
  <li><b>Description:</b> 'Retrieves available moves for a given chess figure on the current field.'</li>
</ul>

Validate Move
<ul>
  <li><b>URL: '/api/v1/&lt;chess_figure&gt;/&lt;current_field&gt;/&lt;dest_field&gt;'</b></li>
  <li><b>Method: 'GET'</b></li>
  <li><b>Description:</b> 'Validates a move for a given chess figure from the current field to the destination field.'</li>
</ul>

<h2>Built With</h2>
<ul>
  <li>Flask - Python web framework</li>
</ul>


<h2>Authors</h2>
<ul>
  <li> <a href="https://github.com/ZbigniewKorycki">Zbigniew Korycki GitHub Profile</a></li>
</ul>

<h2>License</h2>
<ul>
  <li> This project is licensed under the MIT License - see the <a href="https://choosealicense.com/licenses/mit/">LICENSE file</a> for details.</li>
</ul>