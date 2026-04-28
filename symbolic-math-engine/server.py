from flask import Flask, request
from main import evaluate

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Math Engine</title>

            <!-- MathJax for LaTeX rendering -->
            <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

            <style>
                body {
                    font-family: Arial;
                    text-align: center;
                    margin-top: 60px;
                    background-color: #f5f5f5;
                }

                .box {
                    background: white;
                    padding: 25px;
                    display: inline-block;
                    border-radius: 10px;
                    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                }

                input {
                    padding: 10px;
                    margin: 8px;
                    width: 220px;
                }

                button {
                    padding: 10px 20px;
                    cursor: pointer;
                }
            </style>
        </head>

        <body>
            <div class="box">
                <h2>Math Engine</h2>

                <form action="/compute">
                    <input name="expr" placeholder="Expression (e.g. x+2)">
                    <br>
                    <input name="x" placeholder="Value of x (optional)">
                    <br>
                    <button type="submit">Compute</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.route("/compute")
def compute():
    expr = request.args.get("expr")
    xv = request.args.get("x")

    # clean x input
    if xv:
        try:
            xv = float(xv)
        except:
            xv = None
    else:
        xv = None

    result = evaluate(expr, xv)

    return f"""
    <html>
        <head>
            <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        </head>

        <body style="font-family: Arial; text-align:center; margin-top:60px;">
            <h2>Result</h2>

            <p><b>Expression:</b> \\({expr}\\)</p>
            <p><b>Result:</b> {result}</p>

            <br>
            <a href="/">Back</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
