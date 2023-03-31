from selenium import webdriver
import time

try:
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
except:
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
    
account_missing_upvote = []
accounts = ['bozz', 'freewritehouse', 'psyberx', 'ntowl' 'improv', 'preparedwombat', 'kryptodenno', 'tattoodjay', 'senstless', 'enginewitty', 'holoz0r', 'discohedge', 'jongolson']

for account in accounts:
    try:
        posts_url = "https://hive.blog/@{}".format(account)
        driver.get(posts_url)

        first_post_xpath = '//*[@id="posts_list"]/ul/li/div/div[2]/div[2]/h2/a[1]'
        hive_blog_post_url = driver.find_element_by_xpath(first_post_xpath).get_attribute('href')
        relative_post_url = hive_blog_post_url.split(".blog/")[1]

        block_explorer_url = "https://hiveblockexplorer.com/{}".format(relative_post_url)
        driver.get(block_explorer_url)

        time.sleep(5)

        post_voter_accounts_xpath = '//*[@id="tablepost_votes"]/tr/td[1]/a'
        post_voter_accounts = driver.find_elements_by_xpath(post_voter_accounts_xpath)

        sbi_upvote = False
        for post_voter_account in post_voter_accounts:
            if post_voter_account.text in ['@steembasicincome', '@sbi2', '@sbi3', '@sbi4', '@sbi5', '@sbi6', '@sbi7', '@sbi8', '@sbi9']:
                sbi_upvote = True
                break

        if not sbi_upvote:
            print(driver.current_url + " FAILED")
            account_missing_upvote.append(account)
        else:
            print(driver.current_url + " SUCCESS")
    except Exception as e:
        print(driver.current_url + " ERROR:" + str(e))

driver.close()
assert not account_missing_upvote, "The following accounts are missing upvotes: {}" \
                                   "".format(", ".join(account_missing_upvote))
