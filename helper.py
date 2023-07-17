import os

startup = True


def update_qty(session, id, qty_add):
    if qty_add == 0:
        return
    qty_dict = session["qty_dict"].copy()

    new_val = qty_dict.get(id, 0) + int(qty_add)
    if new_val == 0:
        qty_dict.pop(id)
    else:
        qty_dict[id] = new_val
    session["qty_dict"] = qty_dict


def make_qty_zero(session):
    session["qty_dict"] = {}


def init_vars(session):
    global startup

    if startup:
        startup = False

        session["acceptable_cities"] = acceptable_cities
        session["items"] = items
        make_qty_zero(session)


def rename_files():
    os.chdir("static/images/products")
    imgs = os.listdir()
    for img in imgs:
        os.rename(img, str(int(img.replace("png")) - 1) + ".png")


items = [{"name": "Toned Milk", "size": "1L", "image": "0.png", "price": 70, },
         {"name": "Free Range Eggs", "size": "30 pieces", "image": "1.png", "price": 240},
         {"name": "Pasteurized Butter", "size": "100g", "image": "2.png", "price": 50},
         {"name": "Sliced Bread", "size": "400g", "image": "3.png", "price": 50},
         {"name": "Coffee Powder", "size": "200g", "image": "4.png", "price": 300},
         {"name": "Tea", "size": "250g", "image": "5.png", "price": 300},
         {"name": "Bottled Water", "size": "1L", "image": "6.png", "price": 20},
         {"name": "Orange Juice", "size": "1L", "image": "7.png", "price": 120},
         {"name": "Apple Juice", "size": "500ml", "image": "8.png", "price": 55},
         {"name": "Coconut Water", "size": "1L", "image": "9.png", "price": 80},
         {"name": "Mango Drink", "size": "1.2L", "image": "10.png", "price": 75},
         {"name": "Cola", "size": "750ml", "image": "11.png", "price": 35}]
acceptable_cities = ["Lucknow", "Delhi", "Chennai", "Mumbai", "Pune", "Moradabad"]


def set_location(session, location):
    print(location)
    session["location"] = location
    print(location)
    return


"removed code:"
""" HTML:
<form method="POST"> 
<select class="location-drop-down" name="location">
...
<input class="submit-location-btn" name="location" type="submit" value="Change Location">
</form>
"""

""" CSS:
.submit-location-btn {
    background-color: #4CAF50;
    border: none;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    font-family: "Calibri", Times, sans-serif;
}
"""

""" Python:
methods=["POST", "GET"]
if request.method == "POST":
helper.set_location(session, request.form["location"])
return redirect(request.url)
"""
