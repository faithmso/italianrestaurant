tables = {
  1:{
    'name':'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange juice, Apple juice',
      'food_items':'pancakes',
      'total':[534.50,20.0,5]
    },
    
  }
  2:{},
  3:{},
  4:{},
  5:{},
  6:{},
  7:{}

}

def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name']=name
  tables[table_number]['vip_status']=vip_status
  tables[table_number]['order']={}


def assign_food_items(table_number, **order_items):
  food=order_item.get('food')
  drinks=order_item.get('drinks')
  tables[table_number]['order']['food_items']=food
  tables[table_number]['order']['drinks']=drinks


def calculate_price_per_person(total, tip, split):
  total_tip=total*(tip/100)
  split_price=(total+total_tip)/split
  print(split_price)