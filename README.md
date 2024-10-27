<h1> Sales prediction using svm model </h1>
<p>
   Using support vector machine (SVM) i have created this simple which uses the linear kernel to predict sales for an organisation
   i have picked a random dataset from internet and trained this model

</p>
<p>
Since i am using python i have used several libraries here:
 <ul>
            <li>pandas</li>
            <li>sklearn</li>
            <li>matplotlib</li>
            <li>streamlit</li>
 
 </ul>

</p>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Streamlit App Setup Guide</title>
</head>
<body>
  <h1>Streamlit App Setup Guide</h1>
  <p>This guide explains how to activate a Python virtual environment and run a Streamlit application.</p>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.6 or higher installed</li>
    <li>pip (comes with Python)</li>
  </ul>

  <h2>Steps to Setup and Run</h2>

  <h3>1. Create a Virtual Environment</h3>
  <p>Open a terminal or command prompt in your project directory and run:</p>
  <pre>
<code># On Windows
python -m venv venv

# On Linux / macOS
python3 -m venv venv</code>
  </pre>

  <h3>2. Activate the Virtual Environment</h3>
  <pre>
<code># On Windows
.\venv\Scripts\activate

# On Linux / macOS
source venv/bin/activate</code>
  </pre>
  <p>You should see <code>(venv)</code> in your terminal prompt, indicating the virtual environment is active.</p>

  <h3>3. Install Streamlit</h3>
  <p>With the virtual environment activated, run:</p>
  <pre><code>pip install streamlit</code></pre>

  <h3>4. Run the Streamlit App</h3>
  <p>Navigate to the folder containing your app script and execute:</p>
  <pre><code>streamlit run app.py</code></pre>
  <p>Replace <code>app.py</code> with the name of your script if it's different.</p>

  <h3>5. Stop the Streamlit App</h3>
  <p>To stop the app, press <strong>CTRL + C</strong> in the terminal.</p>

  <h3>6. Deactivate the Virtual Environment</h3>
  <pre><code>deactivate</code></pre>

  <h2>Troubleshooting</h2>
  <ul>
    <li><strong>Command not found</strong>: Ensure Python and pip are properly installed and added to your system's PATH.</li>
    <li>Run <code>pip list</code> inside the virtual environment to confirm that Streamlit is installed.</li>
  </ul>

  <p>This README provides basic instructions to help you quickly set up and run your Streamlit app. Happy coding! 🎉</p>
</body>
</html>
