from flask import Flask,jsonify,render_template
import json
import sys

app=Flask(__name__)
dummy_data=[{
"customer_id":1,
"order_id":35335,
"order_date":"7/27/2025 11:01:34 AM",
"cost(in Dollars)":500

},

{
"customer_id":2,
"order_id":35537797,
"order_date":"7/27/2025 11:01:34 AM",
"cost(in Dollars)":700


},
{ "customer_id": 143, "order_id": 45672, "order_date": "7/26/2025 2:15:22 PM", "cost(in Dollars)": 325 },
  { "customer_id": 567, "order_id": 78934521, "order_date": "7/25/2025 9:42:17 AM", "cost(in Dollars)": 1250 },
  { "customer_id": 89, "order_id": 23456789, "order_date": "7/24/2025 4:33:55 PM", "cost(in Dollars)": 875 },
  { "customer_id": 234, "order_id": 56789012, "order_date": "7/23/2025 11:28:41 AM", "cost(in Dollars)": 450 },
  { "customer_id": 456, "order_id": 34567890, "order_date": "7/22/2025 6:15:09 PM", "cost(in Dollars)": 1680 },
  { "customer_id": 78, "order_id": 12345678, "order_date": "7/21/2025 1:52:33 PM", "cost(in Dollars)": 290 },
  { "customer_id": 345, "order_id": 67890123, "order_date": "7/20/2025 8:37:44 AM", "cost(in Dollars)": 750 },
  { "customer_id": 612, "order_id": 45678901, "order_date": "7/19/2025 3:21:56 PM", "cost(in Dollars)": 1420 },
  { "customer_id": 189, "order_id": 23456780, "order_date": "7/18/2025 10:14:27 AM", "cost(in Dollars)": 635 },
  { "customer_id": 423, "order_id": 56789013, "order_date": "7/17/2025 5:48:18 PM", "cost(in Dollars)": 980 },
  { "customer_id": 756, "order_id": 34567891, "order_date": "7/16/2025 12:36:42 PM", "cost(in Dollars)": 540 },
  { "customer_id": 91, "order_id": 12345679, "order_date": "7/15/2025 7:29:53 AM", "cost(in Dollars)": 1150 },
  { "customer_id": 378, "order_id": 67890124, "order_date": "7/14/2025 2:17:35 PM", "cost(in Dollars)": 385 },
  { "customer_id": 524, "order_id": 45678902, "order_date": "7/13/2025 9:43:26 AM", "cost(in Dollars)": 825 },
  { "customer_id": 167, "order_id": 23456781, "order_date": "7/12/2025 4:55:14 PM", "cost(in Dollars)": 1380 },
  { "customer_id": 689, "order_id": 56789014, "order_date": "7/11/2025 11:22:08 AM", "cost(in Dollars)": 475 },
  { "customer_id": 245, "order_id": 34567892, "order_date": "7/10/2025 6:38:49 PM", "cost(in Dollars)": 920 },
  { "customer_id": 831, "order_id": 12345680, "order_date": "7/9/2025 1:16:31 PM", "cost(in Dollars)": 650 },
  { "customer_id": 456, "order_id": 67890125, "order_date": "7/8/2025 8:52:47 AM", "cost(in Dollars)": 1575 },
  { "customer_id": 123, "order_id": 45678903, "order_date": "7/7/2025 3:41:22 PM", "cost(in Dollars)": 295 },
  { "customer_id": 567, "order_id": 23456782, "order_date": "7/6/2025 10:27:39 AM", "cost(in Dollars)": 780 },
  { "customer_id": 789, "order_id": 56789015, "order_date": "7/5/2025 5:14:55 PM", "cost(in Dollars)": 1240 },
  { "customer_id": 234, "order_id": 34567893, "order_date": "7/4/2025 12:58:16 PM", "cost(in Dollars)": 560 },
  { "customer_id": 445, "order_id": 12345681, "order_date": "7/3/2025 7:35:03 AM", "cost(in Dollars)": 890 },
  { "customer_id": 678, "order_id": 67890126, "order_date": "7/2/2025 2:49:28 PM", "cost(in Dollars)": 435 },
  { "customer_id": 198, "order_id": 45678904, "order_date": "7/1/2025 9:23:51 AM", "cost(in Dollars)": 1320 },
  { "customer_id": 521, "order_id": 23456783, "order_date": "6/30/2025 4:17:44 PM", "cost(in Dollars)": 675 },
  { "customer_id": 356, "order_id": 56789016, "order_date": "6/29/2025 11:42:19 AM", "cost(in Dollars)": 1180 },
  { "customer_id": 734, "order_id": 34567894, "order_date": "6/28/2025 6:56:07 PM", "cost(in Dollars)": 405 },
  { "customer_id": 89, "order_id": 12345682, "order_date": "6/27/2025 1:31:52 PM", "cost(in Dollars)": 850 },
  { "customer_id": 412, "order_id": 67890127, "order_date": "6/26/2025 8:18:36 AM", "cost(in Dollars)": 720 },
  { "customer_id": 667, "order_id": 45678905, "order_date": "6/25/2025 3:44:23 PM", "cost(in Dollars)": 1495 },
  { "customer_id": 145, "order_id": 23456784, "order_date": "6/24/2025 10:29:41 AM", "cost(in Dollars)": 380 },
  { "customer_id": 598, "order_id": 56789017, "order_date": "6/23/2025 5:52:15 PM", "cost(in Dollars)": 965 },
  { "customer_id": 283, "order_id": 34567895, "order_date": "6/22/2025 12:15:58 PM", "cost(in Dollars)": 615 },
  { "customer_id": 756, "order_id": 12345683, "order_date": "6/21/2025 7:38:29 AM", "cost(in Dollars)": 1275 },
  { "customer_id": 329, "order_id": 67890128, "order_date": "6/20/2025 2:51:46 PM", "cost(in Dollars)": 495 },
  { "customer_id": 584, "order_id": 45678906, "order_date": "6/19/2025 9:26:33 AM", "cost(in Dollars)": 835 },
  { "customer_id": 167, "order_id": 23456785, "order_date": "6/18/2025 4:43:17 PM", "cost(in Dollars)": 1390 },
  { "customer_id": 692, "order_id": 56789018, "order_date": "6/17/2025 11:17:52 AM", "cost(in Dollars)": 525 },
  { "customer_id": 238, "order_id": 34567896, "order_date": "6/16/2025 6:34:08 PM", "cost(in Dollars)": 755 },
  { "customer_id": 415, "order_id": 12345684, "order_date": "6/15/2025 1:58:24 PM", "cost(in Dollars)": 1160 },
  { "customer_id": 673, "order_id": 67890129, "order_date": "6/14/2025 8:21:39 AM", "cost(in Dollars)": 425 },
  { "customer_id": 156, "order_id": 45678907, "order_date": "6/13/2025 3:47:56 PM", "cost(in Dollars)": 695 },
  { "customer_id": 529, "order_id": 23456786, "order_date": "6/12/2025 10:32:11 AM", "cost(in Dollars)": 1425 },
  { "customer_id": 384, "order_id": 56789019, "order_date": "6/11/2025 5:16:47 PM", "cost(in Dollars)": 580 },
  { "customer_id": 717, "order_id": 34567897, "order_date": "6/10/2025 12:41:32 PM", "cost(in Dollars)": 940 },
  { "customer_id": 198, "order_id": 12345685, "order_date": "6/9/2025 7:54:18 AM", "cost(in Dollars)": 365 },
  { "customer_id": 642, "order_id": 67890130, "order_date": "6/8/2025 2:28:43 PM", "cost(in Dollars)": 810 },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/add")
def addOrders():
    return render_template("add_orders.html")
@app.route("/getcustomerdata",methods=['GET'])
def getdata():
    return  jsonify(dummy_data)

if __name__=="main":
    app.run(host="0.0.0.0",port=5000)