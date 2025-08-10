# Finmanager - track your finances in a browser from any device

Finmanager is a Django web application that lets you track your own finances and budget through adding expenses or incomes to your money accounts.
App features:
- Create your finance accounts (like cash, card etc.);
- Track accounts balances through adding or removing money using incomes or expenses;
- Categorize your incomes or expenses using category system.

Basic TODOs to consider this app usable:
- Implement userless authorization for security;
- Make left navbar be hidden with burger menu;
- Add pagination for transactions;
- Rethink interface for both desktops and mobiles;
- Make first launch script so it will ease first-time launch routine like creating db.

Features ahead:
- Check system: add transactions in a bunch in a convenient way;
- Make single page forms for every type of models (Accounts, Transactions, Checks, Categories);
- Rewrite statistics module so it can analyze in more detailed way;
- Rewrite charts module to stop using chart.js;

# Installation:
You will need django and django-bootstrap5 modules to run this app. Make sure to use python manage.py makemigrations and pthon manage.py migrate in a project's root folder.
