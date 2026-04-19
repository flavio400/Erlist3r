# !/usr/bin/env python3

import time;
import os;
import argparse;
from colorama import Fore, Style;
from itertools import product;

io: str = Fore.RED + 'flavio400' + Style.RESET_ALL;
char1: str = Fore.GREEN + '[+]' + Style.RESET_ALL;
char2: str = Fore.RED + '[!!]' + Style.RESET_ALL;
must_add: str = Fore.RED + 'must-add' + Style.RESET_ALL;
adv: str = char2 + Fore.GREEN + ' Do not add words containing too much equal characters ' + Style.RESET_ALL + char2;

logo: str = rf'''
      _,     ,_     examples:
    .'/  ,_   \'.   python erlist3r.py -i
   |  \__( >__/  |  python erlist3r.py -i -r (to add top 200 from rockyou)
   \             /  
    '-..__ __..-'   erList3r by {io} (2026)
         /_\        targeted list generator for brute-force

{adv}

you might want to look at the {must_add} list:
>> name, surname, nicknames
>> pet names
>> city, home address
>> hobbys, football team
>> old passwords
'''

rockyou: bool = False

parser = argparse.ArgumentParser();

parser.add_argument(
    '-i', '--interactive',
    dest='interactive_mode',
    required=False,
    action='store_true',
    help='python erlist3r.py --i'
)

parser.add_argument(
    '-r', '--rockyou',
    dest='rockyou',
    required=False,
    action='store_true',
    help='python erlist3r.py -r'
)

args = parser.parse_args();

def get_info():
    while True:
        nms: str  = input('[!] insert all the names, nicknames, surnames (no commas, only spaces): ').strip();
        names: tuple = nms.split();

        print(f'{char1} important names accepted: {names}');
        break;
    
    while True:
        dts = input('[!] insert all the dates (DDMMYYYY, no commas, only spaces): ').strip();
        dates: tuple = dts.split()

        valid_dates: list = [];
        for d in dates:
            if d.isdigit():
                if len(d) == 8:
                    valid_dates.append(d);
                else:
                    print(f'{char2} lenght must be eight digits');
                    continue;
            else:
                print(f'{char2} is not a number');
                continue;
    
        print(f'{char1} important dates accepted: {valid_dates}');
        break;

    while True:
        nmbrs = input('[!] insert phone numbers or any other important numbers (no commas, only spaces): ').strip();
        numbers: tuple = nmbrs.split();
    
        valid_numbers: list = [];
        for n in numbers:
            if n.isdigit():
                if len(n) == 10:
                    valid_numbers.append(n);
                else:
                    print(f'{char2} lenght must be ten digits');
                    continue;
            else:
                print(f'{char2} is not a number')
                continue;
        
        print(f'{char1} important numbers accepted: {valid_numbers}');
        break;

    return names, valid_dates, valid_numbers;

def set_params():
    global rockyou;

    if args.rockyou is not None:
        rockyou = True;


def generate():
    dt_names, nm_valid_dates, dt_valid_numbers = get_info()

    leet_permutations: list = {
        'a': ['a', '4', '@'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        's': ['s', '5', '$'],
        't': ['t', '7'],
        'b': ['b', '8'],
        'g': ['g', '9'],
        'l': ['l', '1']
    }

    common_numbers: list = [
    "123", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890",    
    "111", "1111", "111111", "222", "2222", "333", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "000", "0000",   
    "1212", "1313", "1122", "1221", "6969", "420", "42069",   
    "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
    "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
    "2021", "2022", "2023", "2024", "2025", "2026",
    "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999",    
    "69", "666", "777", "888", "999", "000000",
    "12", "21", "23", "32", "45", "54", "67", "99", "89"
    "987654321", "98765", "54321", "4321",    
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
    "11", "22", "33", "44", "55", "66", "77", "88", "99",    
    "2580", "1593", "147258", "369", "147", "258", "369369",    
    "314159", "271828", "007", "008", "009", "1010", "1004", "2001",
    "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "010",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26",
    "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"
]

    top_200_rockyou: list = ["password", "sixseven", "123456", "12345678", "1234", "qwerty", "12345", "dragon", "pussy", "baseball", "football", "letmein", "monkey", "696969", "abc123", "mustang", "michael", "shadow", "master", "jennifer", "111111", "2000", "jordan", "superman", "harley", "1234567", "fuckme", "hunter", "fuckyou", "trustno1", "ranger", "buster", "thomas", "tigger", "robert", "soccer", "fuck", "batman", "test", "pass", "killer", "hockey", "george", "charlie", "andrew", "michelle", "love", "sunshine", "jessica", "asshole", "6969", "pepper", "daniel", "access", "123456789", "654321", "joshua", "maggie", "starwars", "silver", "william", "dallas", "yankees", "123123", "ashley", "666666", "hello", "amanda", "orange", "biteme", "freedom", "computer", "sexy", "thunder", "nicole", "ginger", "heather", "hammer", "summer", "corvette", "taylor", "fucker", "austin", "1111", "merlin", "matthew", "121212", "golfer", "cheese", "princess", "martin", "chelsea", "patrick", "richard", "diamond", "yellow", "bigdog", "secret", "asdfgh", "sparky", "cowboy", "camaro", "anthony", "matrix", "falcon", "iloveyou", "bailey", "guitar", "jackson", "purple", "scooter", "phoenix", "aaaaaa", "morgan", "tigers", "porsche", "mickey", "maverick", "cookie", "nascar", "peanut", "justin", "131313", "money", "horny", "samantha", "panties", "steelers", "joseph", "snoopy", "boomer", "whatever", "iceman", "smokey", "gateway", "dakota", "cowboys", "eagles", "chicken", "dick", "black", "zxcvbn", "please", "andrea", "ferrari", "knight", "hardcore", "melissa", "compaq", "coffee", "booboo", "bitch", "johnny", "bulldog", "xxxxxx", "welcome", "james", "player", "ncc1701", "wizard", "scooby", "charles", "junior", "internet", "bigdick", "mike", "brandy", "tennis", "blowjob", "banana", "monster", "spider", "lakers", "miller", "rabbit", "enter", "mercedes", "brandon", "steven"]

    ultra_list: list = [];

    dt_names_upper: list = [w.capitalize() for w in dt_names];

    def generate_leets(words, max_results=300):
        result: list = [];
        for word in words[:30]:
            variants = [leet_permutations.get(c.lower(), [c.lower()]) for c in word];
            for combo in product(*variants):
                result.append(''.join(combo));
                if len(result) >= max_results:
                    return result;
        return result;

    names_dates: list = [x + y for x in dt_names for y in nm_valid_dates[-6:]];
    names_dates_upper: list = [x.capitalize() + y for x in dt_names for y in nm_valid_dates[-6:]];

    names_numbers: list = [x + y for x in dt_names for y in dt_valid_numbers];
    names_numbers_upper: list = [x.capitalize() + y for x in dt_names for y in dt_valid_numbers];

    dates_names: list = [y + x for x in dt_names for y in nm_valid_dates[-6:]];
    numbers_names: list = [y + x for x in dt_names for y in dt_valid_numbers];

    names_combined: list = [x + y for x in dt_names for y in dt_names[:10]];
    names_combined_upper: list = [x.capitalize() + y.capitalize() for x in dt_names for y in dt_names[:10]];

    nm_leets: list = generate_leets(dt_names, 350);
    leet_names_dates: list = generate_leets(names_dates, 200);
    leet_names_numbers: list = generate_leets(names_numbers, 200);

    triple: list = [];
    for name in dt_names[:15]:
        for date in nm_valid_dates[-5:]:
            for num in dt_valid_numbers[:6]:
                triple.extend([
                    name + date + num,
                    name.capitalize() + date + num,
                    date + name + num,
                    name + num + date,
                    num + name + date
                ]);

    names_dates_title: list = [x.capitalize() + y for x in dt_names for y in nm_valid_dates[-6:]];
    names_numbers_title: list = [x.capitalize() + y for x in dt_names for y in dt_valid_numbers];

    dates_names_upper: list = [y + x.capitalize() for x in dt_names for y in nm_valid_dates[-6:]];
    numbers_names_upper: list = [y + x.capitalize() for x in dt_names for y in dt_valid_numbers];

    triple_light: list = [];
    for name in dt_names[:12]:
        for date in nm_valid_dates[-5:]:
            for num in dt_valid_numbers[:5]:
                triple_light.extend([
                    name + date + num,
                    name.capitalize() + date + num,
                    date + name + num,
                    name + num + date,
                    num[:4] + name + date
                ]);

    triple_date_num: list = []
    for date in nm_valid_dates[-4:]:
        for num in dt_valid_numbers[:6]:
            for name in dt_names[:10]:
                triple_date_num.extend([
                    date + num + name,
                    date + name + num,
                    num + date + name
                ]);

    leet_dates_names: list = generate_leets(dates_names, 150);
    leet_numbers_names: list = generate_leets(numbers_names, 150);

    leet_names_combined: list = generate_leets(names_combined, 100);

    short_dates: list = [d[-2:] for d in nm_valid_dates if len(d) >= 2];
    names_short_date: list = [x + y for x in dt_names for y in short_dates];
    names_short_date_upper: list = [x.capitalize() + y for x in dt_names for y in short_dates];

    for num in common_numbers:
        for name in dt_names[:20]:  
            ultra_list.append(name + num);
            ultra_list.append(name.capitalize() + num);

    for num in common_numbers:
        for name in dt_names[:20]:
            ultra_list.append(num + name);
            ultra_list.append(num + name.capitalize());

    for num in common_numbers[:50]:         
        for name1 in dt_names[:8]:
            for name2 in dt_names[:8]:
                ultra_list.append(name1 + num + name2);
                ultra_list.append(name1.capitalize() + num + name2.capitalize());

    nm_leets = generate_leets(dt_names, 300);
    for num in common_numbers[:30]:
        for leet_name in nm_leets[:150]:
            ultra_list.append(leet_name + num);
            ultra_list.append(leet_name.capitalize() + num);  

    for num in common_numbers[:40]:
        for name in dt_names[:12]:
            for date in nm_valid_dates[-6:]:
                ultra_list.append(name + date + num);
                ultra_list.append(name.capitalize() + date + num);
                ultra_list.append(date + name + num);

    for num in common_numbers[:25]:
        for name in dt_names[:10]:
            for date in nm_valid_dates[-4:]:
                ultra_list.extend([
                    name + num + date,
                    name.capitalize() + num + date,
                    date + num + name,
                    num + name + date,
                    name + date + num
                ]);
    
    names_pairs: list = [x + y for x in dt_names for y in dt_names];
    names_pairs_upper: list = [x.capitalize() + y.capitalize() for x in dt_names for y in dt_names];

    separators: list = ["", "_", ".", "-", " "];
    names_with_sep: list = [];
    for sep in separators:
        for x in dt_names:
            for y in dt_names:
                names_with_sep.append(x + sep + y);
                names_with_sep.append(x.capitalize() + sep + y.capitalize());

    ultra_list.extend([
        dt_names,
        dt_names_upper,
        nm_valid_dates,
        dt_valid_numbers,
        nm_leets,
        names_dates,
        names_dates_upper,
        names_numbers,
        names_numbers_upper,
        dates_names,
        numbers_names,
        names_combined,
        names_combined_upper,
        leet_names_dates,
        leet_names_numbers,
        triple[:1000],
        names_short_date,
        names_short_date_upper,
        leet_names_combined,
        leet_numbers_names,
        leet_dates_names,
        numbers_names_upper,
        dates_names_upper,
        names_numbers_title,
        names_dates_title,
        names_pairs,
        names_pairs_upper,
        names_with_sep
    ]);

    if args.rockyou:
        ultra_list.extend([
            top_200_rockyou
        ]);

    all_passwords: list = [pwd for sublist in ultra_list for pwd in sublist];
    all_passwords: list = list(dict.fromkeys(all_passwords));
    all_passwords = [pwd.replace(' ' , '_') for pwd in all_passwords];

    print(f'generated {len(all_passwords):,} passwords');

    return all_passwords;


def get_path():
    path: str = os.getcwd();
    return path;

def write():
    path = get_path();
    passwords = generate();

    file: str = f'passwords_{time.strftime("%Y%m%d_%H%M%S")}';

    with open(file, 'w', encoding = 'utf-8') as p:
        for password in passwords:
            p.write(f'{password}\n');
    
    print('');
    print(rf'{char1} exact path: {path}{file}');

    ex: str = 'exiting erlist3r';
    print('');
    print('');
    for ch in ex:
        print(Fore.RED + ch + Style.RESET_ALL, end = '', flush = True);
        time.sleep(0.01);
    print('');
    print('');

if __name__ == '__main__':
    try:
        for l in logo:
            print(l, end = '', flush = True);
            time.sleep(0.001);
        print('');

        set_params();

        print(f'rockyou: {rockyou}');
        print('');

        write();

    except KeyboardInterrupt:
        ex: str = 'exiting erlist3r';
        print('');
        print('');
        for ch in ex:
            print(Fore.RED + ch + Style.RESET_ALL, end = '', flush = True);
            time.sleep(0.01);
        print('');
        print('');
