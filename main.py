import time
import csv
from os import times
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
chromedriver_path = r'chromedriver'
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome()
filename = 'config.csv'
column_name = 'value'
values_list = []

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if column_name in row:
            values_list.append(row[column_name])
company_name= values_list[0]
english_b_id = values_list[1]
s_id = int(values_list[2])
e_id = int(values_list[3])
dialer_link= values_list[4]
dpassword= values_list[5]
proc= int(values_list[6])
p2= values_list[7]
p3= values_list[8]
p4= values_list[9]
preset= int(values_list[10])
campain=values_list[11]
c1=values_list[12]
c2=values_list[13]
if c1 == c2 :
    print("please check your valuse!!!!!!!!invalid option")
elif c1 == 'yes':
  list_new_mac_addresses = []
  #pp=english_b_id + str(s_id)
  mac_path='mac.txt'
  with open(mac_path, 'r') as file:
     for line in file:
         line = line.strip()

         if ' ' in line:
             first_part, second_part = line.split(' ', 1)
             second_part = second_part.replace(':', '-')
             list_new_mac_addresses.append(second_part)
         else:
             line = line.replace(':', '-')
             list_new_mac_addresses.append(line)
     total_mac_address = len(list_new_mac_addresses)
  count_ids=0
  for num in range(s_id, e_id + 1):
     count_ids +=1
  if total_mac_address != count_ids :
      print("MacAddresses & Number of Ids does not match")
      print("-------------------END---------------------")
  elif e_id < s_id:
      print("Invlid Ids have been entered")
      print("------------End--------------")
  elif s_id == "" or e_id == "":
      print("Please Insert both starting ids & Ending IDs")
      print("-------------------End----------------------")
  else:
   driver.get("https://www.alpha-avatar.callwise.ai/login")
   input_email_xpath="email"
   search_element = driver.find_element(By.NAME, input_email_xpath)
   search_element.send_keys("support@idrakai.com")
   input_password_xpath ="password"
   search_element = driver.find_element(By.NAME, input_password_xpath)
   search_element.send_keys("security@idrak#")
   submit_button = "/html/body/div/div/div/form/div[5]/button"
   submit_button_element = driver.find_element(By.XPATH, submit_button)
   submit_button_element.click()
   company_button = "/html/body/aside/nav/ul/li[2]/a/i"
   click_element_company= driver.find_element(By.XPATH, company_button)
   click_element_company.click()
   List_companies ="/html/body/aside/nav/ul/li[2]/div/a"
   click_element_company= driver.find_element(By.XPATH, List_companies)
   click_element_company.click()
   print("Selecting company")

#input_scompany_xpath="/html/body/main/section/div[2]/div/div/div/div[2]/label/input"
   search_element = driver.find_element(By.XPATH, '//input[@type="search"]')
   search_element.send_keys(company_name)
   print("Entering into :",company_name)
   time.sleep(4)
   detail_button = "/html/body/main/section/div[2]/div/div/div/table/tbody/tr[1]/td[8]/a"
   click_element_detail= driver.find_element(By.XPATH, detail_button)
   click_element_detail.click()
   time.sleep(4)
   first_id = s_id
   for ids in range(total_mac_address):

      time.sleep(5)
      time.sleep(0.5)
      driver.switch_to.window(driver.window_handles[1])
      search_element = driver.find_element(By.XPATH, '//input[@type="search"]')
      search_element.send_keys(list_new_mac_addresses[ids])
      search_element.clear()
      button_xpath = "/html/body/main/section/div[2]/div/div/div/table/tbody/tr[1]/td[11]/div/a"
      try:
                  click_element_detail = driver.find_element(By.XPATH, button_xpath)
                  # Do something with click_element_detail if it's found
      except NoSuchElementException:
              print(list_new_mac_addresses[ids] , ": Mac not found")
              first_id +=1
      else:
          time.sleep(0.5)
          wait = WebDriverWait(driver, 5)
          click_element_detail.click()
          b_button = "/html/body/main/section/div[2]/div/div/div/table/tbody/tr/td[11]/div/div/a[1]"
          click_element_detail = driver.find_element(By.XPATH, b_button)
          click_element_detail.click()
          time.sleep(5)
          if dialer_link != "":
                  input_dialer = "dialer_url"
                  search_element = driver.find_element(By.NAME, input_dialer)
                  search_element.clear()
                  search_element.send_keys(dialer_link)
          else :
              pass
          if proc != "":
             dropdown_path = "transfer_procedure"
             dropdown_element = driver.find_element(By.NAME, dropdown_path)
             select = Select(dropdown_element)
             option_index_to_select = proc
             select.select_by_index(option_index_to_select)
          else:
             pass
          input_did = "did"
          search_element = driver.find_element(By.NAME, input_did)
          search_element.clear()
          search_element.send_keys("1")
              #dropdown_xpath = "//select[@id='preset_name']"
             #dropdown_path = "preset_name"
             #dropdown_element = driver.find_element(By.NAME, dropdown_path)
             #select.select_by_visible_text(preset)
          if preset != "":
               dropdown_path = "preset_name"
               dropdown_element = driver.find_element(By.NAME, dropdown_path)
               select = Select(dropdown_element)
               option_index_to_select = preset
               select.select_by_index(option_index_to_select)
          else :
              pass

          if campain != "":
                  input_camp= "campaign_no"
                  search_element = driver.find_element(By.NAME, input_camp)
                  search_element.clear()
                  search_element.send_keys(campain)
          else :
              pass
          if english_b_id != "":
             input_id = "username"
             search_element = driver.find_element(By.NAME, input_id)
             search_element.clear()
             search_element.send_keys(english_b_id+str(first_id))
          else:
             input_id = "username"
             search_element = driver.find_element(By.NAME, input_id)
             search_element.clear()
             search_element.send_keys(first_id)
          if dpassword != "":
           if dpassword == str(s_id) :
              input_pass = "password"
              search_element = driver.find_element(By.NAME, input_pass)
              search_element.clear()
              search_element.send_keys(first_id)
           elif dpassword == english_b_id+str(s_id):
              input_pass = "password"
              search_element = driver.find_element(By.NAME, input_pass)
              search_element.clear()
              search_element.send_keys(english_b_id+str(first_id))
           else:
              input_pass = "password"
              search_element = driver.find_element(By.NAME, input_pass)
              search_element.clear()
              search_element.send_keys(dpassword)
          else :
              pass
          c1 = 'pages2'
          checkbox = driver.find_element(By.NAME, c1)

         # Handle pages2 checkbox
          if p2 == "yes":
              if not checkbox.is_selected():  # Check if checkbox is not already selected
                  checkbox.click()
          elif p2 == "no":
              if checkbox.is_selected():  # Check if checkbox is already selected
                  checkbox.click()

          c2 = 'pages3'
          checkbox = driver.find_element(By.NAME, c2)

         # Handle pages3 checkbox
          if p3 == "yes":
              if not checkbox.is_selected():  # Check if checkbox is not already selected
                  checkbox.click()
          elif p3 == "no":
              if checkbox.is_selected():  # Check if checkbox is already selected
                  checkbox.click()

          c3 = 'pages4'
          checkbox = driver.find_element(By.NAME, c3)

         # Handle pages4 checkbox
          if p4 == "yes":
              if not checkbox.is_selected():  # Check if checkbox is not already selected
                  checkbox.click()
          elif p4 == "no":
              if checkbox.is_selected():  # Check if checkbox is already selected
                  checkbox.click()

          dropdownpath = "status"
          dropdown_element = driver.find_element(By.NAME, dropdownpath)
          select = Select(dropdown_element)
          option_to_select = 0
          select.select_by_index(option_to_select)
          button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#prModalLongDialer > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(3) > button:nth-child(2)")))
          button.click()
          concatinate= english_b_id + str(first_id)
          print("MacAddress:", list_new_mac_addresses[ids], "have been registerd against ID:", concatinate)
          first_id = first_id+1
  print("All IDS HAVE BEEN REGISTERED")
  print("------------END--------------")
elif c2 == 'yes':
    if s_id == "" or s_id == e_id or e_id < s_id or e_id == "":
     print("Invalid inputs kindly confirm config")
    else :
     f_id = s_id
     driver.get("https://www.alpha-avatar.callwise.ai/login")
     input_email_xpath = "email"
     search_element = driver.find_element(By.NAME, input_email_xpath)
     search_element.send_keys("support@idrakai.com")
     input_password_xpath = "password"
     search_element = driver.find_element(By.NAME, input_password_xpath)
     search_element.send_keys("security@idrak#")
     submit_button = "/html/body/div/div/div/form/div[5]/button"
     submit_button_element = driver.find_element(By.XPATH, submit_button)
     submit_button_element.click()
     company_button = "/html/body/aside/nav/ul/li[2]/a/i"
     click_element_company = driver.find_element(By.XPATH, company_button)
     click_element_company.click()
     List_companies = "/html/body/aside/nav/ul/li[2]/div/a"
     click_element_company = driver.find_element(By.XPATH, List_companies)
     click_element_company.click()
     print("Selecting company")

    # input_scompany_xpath="/html/body/main/section/div[2]/div/div/div/div[2]/label/input"
     search_element = driver.find_element(By.XPATH, '//input[@type="search"]')
     search_element.send_keys(company_name)
     print("Entering into :", company_name)
     time.sleep(4)
     detail_button = "/html/body/main/section/div[2]/div/div/div/table/tbody/tr[1]/td[8]/a"
     click_element_detail = driver.find_element(By.XPATH, detail_button)
     click_element_detail.click()
     time.sleep(4)
     count_ids = 0
     for num in range(s_id, e_id + 1):
         count_ids += 1
     for ids in range(count_ids):
         time.sleep(5)
         time.sleep(0.5)
         driver.switch_to.window(driver.window_handles[1])
         search_element = driver.find_element(By.XPATH, '//input[@type="search"]')
         if english_b_id != "":
             search_element.send_keys(english_b_id+str(f_id)+" "+dialer_link)
         else :
             search_element.send_keys(str(f_id) + " " + dialer_link)
         search_element.clear()
         try:
             element = driver.find_element(By.XPATH,"/html/body/main/section/div[2]/div/div/div/table/tbody/tr/td[3]")
             text_content = element.text
             print(str(f_id)+" "+text_content)
             f_id = f_id + 1

         except NoSuchElementException:
             print(str(f_id)+"  :Mac not found")
             f_id = f_id + 1
         print("Scrapping Completed Successfully!")
else:
    print("kindly choose a type i:e active new ids,scrap mac")
