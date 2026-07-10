from app.ai.analyzer import analyze_sales_call

transcript = """
Advisor:
Good morning, sir.

We are offering an unlimited data plan with 5G.

Customer:
I already use another provider.

Advisor:
Would you consider switching if the monthly cost is lower?
"""

result = analyze_sales_call(transcript)

print(result)