from flask import Flask, render_template_string, request
app = Flask(__name__)

html = """
<div class = "form">
    <form action="{{url_for('sent')}}" method="POST">
        <input placeholder="Enter a line" type="text" name="text">
        <button class="go-button" type="submit"> Submit </button>
    </form>
</div>
"""