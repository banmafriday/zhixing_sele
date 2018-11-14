from appcase.common.base import BaseApp


class MyPage(BaseApp):
    '''页面元素抓取'''
    loc1 = {"name": "我的", "by": "text", "value": "我的" }
    loc2 = {"name": "我的-出行服务", "by": "text", "value": "出行服务"}
    loc3 = {"name": "我的-邀请好友", "by": "text", "value": "一起来抢票"}
    loc4 = {"name": "我的-消息中心", "by": "text", "value": "消息中心"}
    loc5 = {"name": "我的-产品意见", "by": "text", "value": "产品意见"}
    loc6 = {"name": "我的-微信通知", "by": "text", "value": "微信通知"}
    loc7 = {"name": "我的-微信通知", "by": "text", "value": "更多"}
    loc8 = {"name": "我的-加速包", "by": "text", "value": "加速包"}
    loc9 = {"name": "我的-优惠券", "by": "text", "value": "优惠券"}
    loc10 = {"name": "我的-抢票券", "by": "text", "value": "抢票券"}
    loc11 = {"name": "我的-中间banner", "by": "id", "value": "com.yipiao:id/vip_recommend_image"}


    def click_my(self):
        self.click(self.loc1)

class YaoQingHaoYou():
    '''页面元素抓取'''
    tanchu = {"by": "id", "value": "com.yipiao:id/socialize_text_view"}
    quxiao = {"name": "取消分享", "by": "text", "value": "取消分享"}

