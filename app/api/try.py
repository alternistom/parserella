# Python code to sort the tuples using second element  
# of sublist Function to sort using sorted() 
def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    return(sorted(sub_li, key = lambda x: x[4]))     
  
# Driver Code 
sub_li =[['Morgan Stanley Insight Fund', '1002427', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1002427', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1002427/0001752724-20-008413-index.htm'], ['AB GLOBAL REAL ESTATE INVESTMENT FUND INC', '1018368', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1018368', 'NPORT-P', '2020-01-07', 'https://www.sec.gov/Archives/edgar/data/1018368/0001752724-20-002122-index.htm'], ['EATON VANCE GROWTH TRUST', '102816', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=102816', 'NPORT-P', '2020-01-22', 'https://www.sec.gov/Archives/edgar/data/102816/0001752724-20-007708-index.htm'], ['EATON VANCE GROWTH TRUST', '102816', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=102816', 'NPORT-P', '2020-01-22', 'https://www.sec.gov/Archives/edgar/data/102816/0001752724-20-007712-index.htm'], ['EATON VANCE MUNICIPAL INCOME TRUST', '1074540', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1074540', 'NPORT-P', '2020-01-22', 'https://www.sec.gov/Archives/edgar/data/1074540/0001752724-20-007710-index.htm'], ['EATON VANCE NEW YORK MUNICIPAL INCOME TRUST', '1074685', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1074685', 'NPORT-P', '2020-01-22', 'https://www.sec.gov/Archives/edgar/data/1074685/0001752724-20-007714-index.htm'], ['EATON VANCE CALIFORNIA MUNICIPAL INCOME TRUST', '1074692', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1074692', 'NPORT-P', '2020-01-22', 'https://www.sec.gov/Archives/edgar/data/1074692/0001752724-20-007709-index.htm'], ['AB CORE OPPORTUNITIES FUND INC.', '1090504', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1090504', 'NPORT-P', '2020-01-07', 'https://www.sec.gov/Archives/edgar/data/1090504/0001752724-20-002097-index.htm'], ['ARBITRAGE FUNDS', '1105076', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1105076', 'NPORT-P', '2020-01-08', 'https://www.sec.gov/Archives/edgar/data/1105076/0001752724-20-002342-index.htm'], ['ARBITRAGE FUNDS', '1105076', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1105076', 'NPORT-P', '2020-01-08', 'https://www.sec.gov/Archives/edgar/data/1105076/0001752724-20-002343-index.htm'], ['ARBITRAGE FUNDS', '1105076', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1105076', 'NPORT-P', '2020-01-08', 'https://www.sec.gov/Archives/edgar/data/1105076/0001752724-20-002344-index.htm'], ['ARBITRAGE FUNDS', '1105076', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1105076', 'NPORT-P', '2020-01-08', 'https://www.sec.gov/Archives/edgar/data/1105076/0001752724-20-002345-index.htm'], ['BNY MELLON FUNDS TRUST', '1111565', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1111565', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1111565/0001775697-20-000142-index.htm'], ['BNY MELLON FUNDS TRUST', '1111565', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1111565', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1111565/0001775697-20-000143-index.htm'], ['BNY MELLON FUNDS TRUST', '1111565', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1111565', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1111565/0001775697-20-000144-index.htm'], ['BNY MELLON FUNDS TRUST', '1111565', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1111565', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1111565/0001775697-20-000145-index.htm'], ['BNY MELLON FUNDS TRUST', '1111565', 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=1111565', 'NPORT-P', '2020-01-23', 'https://www.sec.gov/Archives/edgar/data/1111565/0001775697-20-000146-index.htm']] 
print(Sort(sub_li))

