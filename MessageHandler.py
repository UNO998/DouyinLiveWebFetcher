class MessageHandler:
    @staticmethod
    def handle_chat(message) -> None:
        """处理聊天消息"""
        user_name = message.user.nick_name
        user_id = message.user.id
        content = message.content
        print(f"[聊天] {user_name}({user_id}): {content}")
    
    @staticmethod
    def handle_gift(message) -> None:
        """处理礼物消息"""
        user_name = message.user.nick_name
        gift_name = message.gift.name
        gift_cnt = message.combo_count
        print(f"[礼物] {user_name} 赠送 {gift_name} x{gift_cnt}")
    
    @staticmethod
    def handle_like(message) -> None:
        """处理点赞消息"""
        user_name = message.user.nick_name
        count = message.count
        print(f"[点赞] {user_name} 点了{count}个赞")
    
    @staticmethod
    def handle_member(message) -> None:
        """处理进入直播间消息"""
        user_name = message.user.nick_name
        user_id = message.user.id
        gender = ["女", "男"][message.user.gender]
        print(f"[进入] {user_name}({user_id}) 进入直播间 性别:{gender}")
    
    @staticmethod
    def handle_social(message) -> None:
        """处理关注消息"""
        user_name = message.user.nick_name
        user_id = message.user.id
        print(f"[关注] {user_name}({user_id}) 关注了主播")
    
    @staticmethod
    def handle_room_stats(message) -> None:
        """处理直播间统计信息"""
        current = message.total
        total = message.total_pv_for_anchor
        print(f"[统计] 当前观看: {current} 总观看: {total}")
    
    @staticmethod
    def handle_fansclub(message) -> None:
        """处理粉丝团消息"""
        content = message.content
        print(f"[粉丝团] {content}")
    
    @staticmethod
    def handle_control(message) -> bool:
        """处理直播间控制消息"""
        if message.status == 3:
            print("[系统] 直播已结束")
            return True
        return False
    
    @staticmethod
    def handle_emoji_chat(message) -> None:
        """处理表情消息"""
        user_name = message.user.nick_name
        emoji_id = message.emoji_id
        content = message.default_content
        print(f"[表情] {user_name} 发送表情({emoji_id}): {content}")
    
    @staticmethod
    def handle_room_message(message) -> None:
        """处理直播间消息"""
        room_id = message.common.room_id
        print(f"[房间] 直播间ID: {room_id}")
    
    @staticmethod
    def handle_room_stats_message(message) -> None:
        """处理直播间统计消息"""
        display_long = message.display_long
        print(f"[房间统计] {display_long}")
    
    @staticmethod
    def handle_rank(message) -> None:
        """处理排行榜消息"""
        ranks = message.ranks_list
        print(f"[排行] {ranks}") 


    @staticmethod
    def handle_control_message(message) -> None:
        """处理直播间状态消息"""
        if message.status == 3:
            print("[系统] 直播间已结束")
            return True
        return False