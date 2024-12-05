from typing import List, Tuple
from pydantic import BaseModel

class Rule(BaseModel):
    x: int
    y: int

class PageOrder(BaseModel):
    pages: List[int]

class InputData(BaseModel):
    rules: List[Rule]
    page_orders: List[PageOrder]

def correct_middle_pages(data:str) -> int:
    input_data = parse_input(data)
    running_sum = 0
    for page in input_data.page_orders:
        if is_page_correct(page, input_data.rules):
            if len(page.pages) == 0:
                continue
            running_sum += get_middle_page(page)
    return running_sum

def fix_incorrect_middle_pages(data:str) -> int: 
    input_data = parse_input(data)
    running_sum = 0
    for page in input_data.page_orders:
        if not is_page_correct(page, input_data.rules):
            if len(page.pages) == 0:
                continue
            corrected_page = correct_page_order(page, input_data.rules)
            running_sum += get_middle_page(corrected_page)
    return running_sum

def correct_page_order(page_order: PageOrder, rules: List[Rule]) -> PageOrder:
    """
    The page order is incorrect, reorder the pages so that the rules are followed
    """
    relevant_rules = [rule for rule in rules if rule.x in page_order.pages and rule.y in page_order.pages]
    def recurse(page_order: PageOrder) -> PageOrder:
        if is_page_correct(page_order, relevant_rules):
            return page_order
        new_page_order = page_order.pages.copy()
        for rule in relevant_rules:
            x_index = new_page_order.index(rule.x)
            y_index = new_page_order.index(rule.y)
            if x_index > y_index:
                new_page_order[x_index], new_page_order[y_index] = new_page_order[y_index], new_page_order[x_index]
        return recurse(PageOrder(pages=new_page_order))
    return recurse(page_order)

def is_page_correct(page_order: PageOrder, rules: List[Rule]) -> bool:
    for rule in rules:
        if rule.x in page_order.pages and rule.y in page_order.pages:
            # get the index of x and y in the page order
            x_index = page_order.pages.index(rule.x)
            y_index = page_order.pages.index(rule.y)
            if x_index > y_index:
                return False
    return True

def get_middle_page(page_order: PageOrder) -> int:
    # get the middle page of a page order
    return page_order.pages[len(page_order.pages) // 2]

def parse_input(data: str) -> InputData:
    # get rules, page_orders 
    # Rules are all before a blank line
    rules_str, page_orders_str = data.split("\n\n")
    rules = rules_str.split("\n")
    page_orders = page_orders_str.split("\n")
    out_rules = []
    for rule in rules:
        x, y = rule.split("|")
        out_rules.append(Rule(x=int(x), y=int(y)))
    out_page_orders = []
    for page_order in page_orders:
        pages = page_order.split(",")
        # convert to list of int
        pages = [int(page) for page in pages if page]
        out_page_orders.append(PageOrder(pages=pages))
    return InputData(rules=out_rules, page_orders=out_page_orders)

def main():
    with open("input.txt") as f:
        data = f.read()
    print(correct_middle_pages(data))
    print(fix_incorrect_middle_pages(data))

if __name__ == "__main__":
    main()
