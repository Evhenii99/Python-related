import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})


class InStock:
    def __init__(self, content):
        self.content = content

    def remainder(self):
        df.loc[df["id"] == self.content, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)


class Output:
    def create(self, article):
        content = df.loc[df["id"] == article].squeeze()

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{content['id']}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {content['name'].title()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {content['price']}", ln=1)

        pdf.output("receipt.pdf")


print(df)
user_id = input("Choose an article to buy: ")
in_stock = InStock(user_id)
in_stock.remainder()
output = Output()
output.create(user_id)
