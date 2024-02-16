import ampdata
import pandas as pd

token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJnUzJBWWh0WjBTbmxFUkZ1UkRWMEZ6d290eW9ZTHJsYlBzR3N3SFlPQ2JjIn0.eyJleHAiOjE3MDc3NDc1MzgsImlhdCI6MTcwNzMxNTY5NywiYXV0aF90aW1lIjoxNzA3MzE1NTM4LCJqdGkiOiIwMTk3Y2UwMy04MTE3LTRhNTgtODFjYS05NWU3YjQwNGQzNTYiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLmxhYi5hbXBpYXRvLmNvbS9yZWFsbXMvbWFzdGVyIiwic3ViIjoiZGUyZWIyMGEtZTZhNS00NWE4LTljMzMtMzIwOGEwNzhiZTRiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYW1wZGF0YSIsIm5vbmNlIjoiN2EyYWIzNjQtMDRlOS00MTAyLTk4ODctZjMyZjJiZGFkMWFkIiwic2Vzc2lvbl9zdGF0ZSI6ImNmNTQ0NjkxLTZiYTYtNGI3OC1iZGMyLWJhOGU5MzM5NDUyZSIsImFjciI6IjAiLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYW1wZGF0YSI6eyJyb2xlcyI6WyJEYXRhIGJyb3dzZXIiLCJTcG90RXgiLCJNZXJpdCBPcmRlciIsIkFuY2lsbGFyeSBTZXJ2aWNlcyIsIkZvcndhcmQgTWFya2V0Il19fSwic2NvcGUiOiJhbXBkYXRhIHByb2ZpbGUgZW1haWwgb3BlbmlkIiwic2lkIjoiY2Y1NDQ2OTEtNmJhNi00Yjc4LWJkYzItYmE4ZTkzMzk0NTJlIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJUb21hcyBLcmVqY2kiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0b21hcy5rcmVqY2kiLCJnaXZlbl9uYW1lIjoiVG9tYXMiLCJmYW1pbHlfbmFtZSI6IktyZWpjaSIsImVtYWlsIjoidG9tYXMua3JlamNpQGFtcGlhdG8uY29tIn0.yEycGa5CzfKaiwuDgr0lj9BbhvnPEiYnsdAstDUKqyUyZ8GZi4x-VzQGodBMKI1g2gp4Au5BlpwCkeApnUbfwcweQuWpF8VsZACh8sNCi0k8Xlmoo3bWHtkD9x1Y7oPi8K02N55GSQQmVrlAMDtS85ojhYDdsXVJzK12FYnXKY-MaTi6xBgqCkIk7-dxdgy7QDqirsFgmh2yvXWbJDB3M5Ewsg11gB-oyqEl8y6qmqi6eKnza2yOnQqP6B8qLE25Hb3TdeWO0-prkMLgrhCQSRBojqkjvWeM-FzDIkir4IY0gv8quVKx_ym9mu0NXsPRoy4H2M3gOeVnQ6LPf57Ckw"

session = ampdata.Session(urlbase="http://localhost:3000", token=token)

# curves = session.search(query="pri cz power fwd")
# data = {print(c.name): c.get_data().to_pandas() for c in curves}

curve = session.get_curve(name="pri cz power fwd cal25 base eur/mwh d a")
data = curve.get_data(
    data_from=pd.to_datetime("2024-01-01").tz_localize("CET"), data_to="2024-01-15"
)
print(data.to_pandas())
