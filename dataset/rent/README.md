# RentTheRunway

Original link: https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit

| Dataset           | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type           | TimeStamp | User Context | Item Context | Interaction Context |
|-------------------|-----------|-----------|--------------|----------|----------------------------|-----------|--------------|--------------|---------------------|
| RentTheRunway                              | 105,571    | 5,850      | 192,544   | 99\.9688% | Rating<br/> \[0,10\] | √ | √ | √ | √ |

**Description**

These datasets contain measurements of clothing fit from RentTheRunway.

**Basic statistics**
RentTheRunway
Number of users:	105,508
Number of items:	5,850
Number of transactions:	192,544

**Metadata**

- ratings and reviews
- fit feedback (small/fit/large etc.)
- user/item measurements
- category information

**Example (RentTheRunway)**

```yaml
{
  "fit": "fit",
  "user_id": "420272",
  "bust size": "34d",
  "item_id": "2260466",
  "weight": "137lbs",
  "rating": "10",
  "rented for": "vacation",
  "review_text": "An adorable romper! Belt and zipper were a little hard to navigate in a full day of wear/bathroom use, but that's to be expected. Wish it had pockets, but other than that-- absolutely perfect! I got a million compliments.",
  "body type": "hourglass",
  "review_summary": "So many compliments!",
  "category": "romper",
  "height": "5' 8\"",
  "size": 14,
  "age": "28",
  "review_date": "April 20, 2016"
}
```

**Download links**
[Renttherunway](http://deepx.ucsd.edu/public/jmcauley/renttherunway/renttherunway_final_data.json.gz) (31mb)

**Citation**
Please cite the following if you use the data:

Decomposing fit semantics for product size recommendation in metric spaces
Rishabh Misra, Mengting Wan, Julian McAuley
RecSys, 2018
[pdf](https://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18e.pdf)