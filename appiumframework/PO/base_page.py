class Action(object):
    #初始化
    def __init__(self,se_driver):
        self.driver = se_driver

    #重寫元素定位的方法
    def find_element(self,loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s"%(loc))
