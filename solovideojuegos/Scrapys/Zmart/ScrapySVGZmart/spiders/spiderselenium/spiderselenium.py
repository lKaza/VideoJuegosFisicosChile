from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
chrome_path = r"C:\Users\Turbox\Desktop\Nueva carpeta\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.zmart.cl/JuegosPS4")
wait = WebDriverWait(driver, 10)

while True:
    juegos = driver.find_elements_by_xpath("""//*[@class="BoxProductoS2 BorderPlatPS4"]""")
    for juegos1 in juegos:
                i=1
                codigo = driver.find_element_by_xpath("""//*/div[@id="ProdDisplayType5_32641"]/div[@id="ProdDisplayType5_32641_Products"]/div["""+str(i)+"""]/@id""")
                link = driver.find_element_by_xpath("""//div[@id='"""+codigo.text+"""'][@class='BoxProductoS2 BorderPlatPS4']/div[@class="BoxProductoS2_Descripcion"]/a""")
                for linkerinos in link:
                    print(linkerinos)
    print(juegos1.text)
    driver.find_element_by_xpath("""//*[@id="ProdDisplayType5_MasProductos_32641"]/p""").click()
    try:
         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ProdDisplayType5_MasProductos_32641"]/p")]'))).click()
    except TimeoutException:
        break
