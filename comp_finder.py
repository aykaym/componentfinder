from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbjank import Motherboard, GPU, PSU, RAM, CPU, Case, Drive, Base
import openpyxl

wb = openpyxl.Workbook()
filename = "parts.xlsx"

def get_items(keyword):
    token = open("token.txt", 'r').read().replace("/n", '')

    try:
        api = Finding(appid=token, config_file=None)
        response = api.execute('findItemsAdvanced', {
                                    'keywords': keyword,
                                    'paginationInput':
                                        {'entriesPerPage':'100'}
                                })
        search = response.dict()
        parse_items(keyword, search)



    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def parse_items(keyword, search):
    listings = []
    for item in search['searchResult']['item']:
        listing = []
        title = item['title']
        mop = item['paymentMethod']
        current_price = item['sellingStatus']['currentPrice']['value']
        if item['shippingInfo']['shippingType'] == "Free":
            shipping = item['shippingInfo']['shippingServiceCost']['value']
        else:
            shipping = "Calculated"
        url = item['viewItemURL']
        hyperlink = "=HYPERLINK(\""+url+"\",\"Link\")"
        if 'condition' in item:
            condition = item['condition']['conditionDisplayName']
        else:
            condition = "N/A"
        endTime = item['listingInfo']['endTime']
        listing.extend([hyperlink, title, current_price, shipping, condition, endTime])
        listings.append(listing)
    create_xlsx(keyword, listings)

def create_xlsx(keyword, listings):
    array = ["URL", "Title", "Current Price", "Shipping Cost", "Condition", "End Date"]
    ws2 = wb.create_sheet(title=keyword)
    ws2.append(array)
    for listing in listings:
        ws2.append(listing)

    match_parts(keyword, listings)


def match_parts(keyword, listings):
    engine = create_engine('sqlite:///parts.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    cpus = session.query(CPU)
    #mobos = session.query(Motherboard)
    #memories = session.query(RAM)
    #gpus = session.query(GPU)
    #cases = session.query(Case)
    #psus = session.query(PSU)

    for listing in listings:
        title = listing[1]
        current_price = listing[2]
        for cpu in cpus:
            if cpu.model in listing[1]:
                print(cpu.model+ " found in "+ title)
                print("New: " + cpu.price)
                print("Ebay: " + current_price)
                print("-" * 120)



def main():

    keywords = ["Intel processors",
                "Intel socket motherboards",
                "AMD processors",
                "AMD socket motherboards",
                "Nvidia Graphics Card",
                "AMD Graphics Card",
                "1TB HDD",
                "1TB SSD",
                "1TB M2",
                "Gaming Computer Case",
                "8GB DDR3 RAM",
                "8GB DDR4 RAM",
                "Gaming Computers"
                ]

    for keyword in keywords:
        get_items(keyword)

    wb.save(filename=filename)

if __name__ == "__main__":
    main()