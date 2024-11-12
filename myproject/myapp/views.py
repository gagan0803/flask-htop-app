from django.http import HttpResponse
import os
import datetime
import subprocess
import pytz

def htop(request):
    # Get server username
    username = os.getenv("USER", "unknown user")

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format response
    response = f"""
    <h1>Server Information</h1>
    <p><strong>Name:</strong> GAGAN ACHARYA G</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre><strong>Top Output:</strong>\n{top_output}</pre>
    """
    return HttpResponse(response)

