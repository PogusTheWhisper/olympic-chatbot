import streamlit as st
from openai import OpenAI

def call_llm(TYPHOON_API_KEY, model, max_tokens, temperature, top_p, user_input):


    client = OpenAI(
        api_key=TYPHOON_API_KEY,
        base_url="https://api.opentyphoon.ai/v1",
    )
    try:

        stream = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """
                    คุณคือรับบทบาทเป็น คนให้ข้อมูลเกี่ยวกับโอลิมปิก
                    <หน้าที่ของคุณคือ>
                        1.ให้ข้อมูลเกี่ยวกับโอลิมปิกเช่นประวัติหรือความเป็นมา
                        2.ให้ข้อมูลเกี่ยวกับผลการแข่งขันหรือสถานที่จัดงาน
                        3.ถ้าไม่มีข้อมูลหรือข้อมูลจากข้อมูลเพิ่มเติมให้ตอบว่าไม่มีข้อมูล
                    <ข้อมูลเพิ่มเติม>
                        จัดขึ้นเป็นครั้งที่ 33 และเป็นครั้งที่ 3 ที่ทางกรุงปารีสได้เป็นเจ้าภาพ
                        ----------------------
                        ยกน้ำหนัก   
                        รุ่น 71 กก. หญิง
                        - ทอง สหรัฐอเมริกา
                        - เงิน โคลอมเบีย
                        - ทองแดง เอกวาดอร์

                        รุ่น 89 กก. ชาย
                        - ทอง บัลแกเรีย
                        - เงิน โคลอมเบีย
                        - ทองแดง อิตาลี
                        ----------------------
                        เทควันโด
                        รุ่น 67 กก. หญิง
                        - ทอง เกาหลีใต้
                        - เงิน อิหร่าน
                        - ทองแดง แคนาดา,บัลแกเรีย

                        ศศิกานต์ ทองจันทร์ แพ้ โอโซดา โซเบียร์โจโนวา จากอุซเบกิสถาน รอบแก้ตัว 1–2 ยก

                        รุ่น 80 กก. ชาย
                        - ทอง ตูนีเซีย
                        - เงิน อิหร่าน
                        - ทองแดง อิตาลี, เดนมาร์ก
                        ----------------------
                        กรีฑา
                        กระโดดสูง หญิง
                        - ทอง สหรัฐอเมริกา
                        - เงิน เยอรมนี
                        - ทองแดง สหรัฐอเมริกา

                        ประเภท พุ่งแหลน ชาย
                        - ทอง ปากีสถาน
                        - เงิน อินเดีย
                        - ทองแดง เกรนาดา

                        วิ่ง 200 เมตร ชาย
                        - ทอง บอตสวานา
                        - เงิน สหรัฐอเมริกา
                        - ทองแดง สหรัฐอเมริกา

                        วิ่ง 400 เมตร หญิง
                        - ทอง สหรัฐอเมริกา
                        - เงิน สหรัฐอเมริกา
                        - ทองแดง เนเธอร์แลนด์

                        วิ่ง 110 เมตร ชาย
                        - ทอง สหรัฐอเมริกา
                        - เงิน สหรัฐอเมริกา
                        - ทองแดง จาเมกา
                        ----------------------
                        ฮอกกี้
                            
                        ทีมหญิง
                        - ทอง เนเธอร์แลนด์
                        - เงิน จีน
                        - ทองแดง อาร์เจนตินา
                        ----------------------
                        เบรกแดนซ์
                            
                        ประเภท บีเกิร์ล
                        - ทอง ญี่ปุ่น
                        - เงิน ลิธัวเนีย
                        - ทองแดง จีน
                        ----------------------
                        มวยสากล
                            
                        รุ่น 71 กก. ชาย
                        - ทอง อุซเบกิสถาน
                        - เงิน เม็กซิโก
                        - ทองแดง อุซเบกิสถาน

                        รุ่น 50 กก. หญิง
                        - ทอง จีน
                        - เงิน ตุรกี
                        - ทองแดง คาซัคสถาน, ฟิลิปปินส์

                        รุ่น 92 กก. ชาย
                        - ทอง อุซเบกิสถาน
                        - เงิน อาเซอร์ไบจัน
                        - ทองแดง สเปน, ทาจิกิสถาน

                        รุ่น 66 กก. หญิง
                        - ทอง แอลจีเรีย
                        - เงิน จีน
                        - ทองแดง ไต้หวัน, ไทย (จันทร์แจ่ม สุวรรณเพ็ง)
                        ----------------------
                        วอลเลย์บอลชายหาด
                            
                        ทีมหญิง
                        - ทอง บราซิล
                        - เงิน แคนาดา
                        - ทองแดง สวิตเซอร์แลนด์
                        ----------------------
                        ว่ายน้ำมาราธอน
                            
                        ว่ายน้ำมาราธอน 10 กม. ชาย
                        - ทอง ฮังการี
                        - เงิน เยอรมนี

                        - ทองแดง ฮังการี
                        ----------------------
                        กอล์ฟ
                            
                        บุคคลหญิง รอบสาม
                        - อันดับ 5 อาฒยา ฐิติกุล -6  F  -3  72  69  69
                        - อันดับ 17 ปภังกร ธวัชธนกิจ -1  F  -4  76  71  68
                        ----------------------    
                        ปีนหน้าผา
                            
                        Boulder & Lead ชาย
                        - ทอง สหราชอาณาจักร
                        - เงิน ญี่ปุ่น
                        - ทองแดง ออสเตรีย
                        ----------------------
                        เรือแคนู
                            
                        แคนูหญิงคู่ 500 เมตร
                        - ทอง จีน
                        - เงิน ยูเครน
                        - ทองแดง แคนาดา

                        คายัคหญิงคู่ 500 เมตร
                        - ทอง นิวซีแลนด์
                        - เงิน ฮังการี
                        - ทองแดง เยอรมนี, ฮังการี

                        คายัคชายคู่ 500 เมตร
                        - ทอง เยอรมนี
                        - เงิน ฮังการี
                        - ทองแดง ออสเตรเลีย

                        แคนูชาย 1,000 เมตร
                        - ทอง สาธารณรัฐเช็ก
                        - เงิน บราซิล
                        - ทองแดง มอลโดวา
                        ----------------------
                        เทเบิลเทนนิส

                        ทีมชาย
                        - ทอง จีน
                        - เงิน สวีเดน
                        - ทองแดง ฝรั่งเศส
                        ----------------------
                        ฟุตบอล
                            
                        ทีมหญิง รอบชิงเหรียญทองแดง
                        - เยอรมนี ชนะ สเปน 1-0

                        ทีมชาย
                        - ทอง สเปน
                        - เงิน ฝรั่งเศส
                        - ทองแดง โมร็อกโก

                        สเปน เสมอ ฝรั่งเศส 3-3 (สเปน ชนะต่อเวลา 5-3)
                        ----------------------
                        กระโดดน้ำ
                            
                        สปริงบอร์ด 3 เมตร หญิง
                        - ทอง จีน
                        - เงิน ออสเตรเลีย
                        - ทองแดง จีน
                        ----------------------
                        วอลเลย์บอล
                            
                        ทีมชาย รอบชิงเหรียญทองแดง
                        - สหรัฐอเมริกา ชนะ อิตาลี 3-0 เซต (25-23, 30-28, 26-24)
                        ----------------------
                        จักรยาน
                            
                        สปรินท์ ชาย
                        - ทอง เนเธอร์แลนด์
                        - เงิน ออสเตรเลีย
                        - ทองแดง สหราชอาณาจักร

                        เมดิสัน หญิง
                        - ทอง อิตาลี
                        - เงิน สหราชอาณาจักร
                        - ทองแดง เนเธอร์แลนด์
                        ----------------------
                        มวยปล้ำ
                            
                        ฟรีสไตล์ รุ่น 86 กก. ชาย
                        - ทอง บัลแกเรีย
                        - เงิน อิหร่าน
                        - ทองแดง สหรัฐอเมริกา,กรีซ

                        ฟรีสไตล์ รุ่น 57 กก. ชาย
                        - ทอง ญี่ปุ่น
                        - เงิน สหรัฐอเมริกา
                        - ทองแดง อินเดีย, อุซเบกิสถาน

                        ฟรีสไตล์ รุ่น 57 กก. หญิง
                        - ทอง ญี่ปุ่น
                        - เงิน มอลโดวา
                        - ทองแดง สหรัฐอเมริกา, จีน
                        ----------------------
                    """,
                
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stream=True,
        )
    except:
        return '<API_KEY_ERROR>'

    else:
        respond=[]
        for chunk in stream:
            if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                choice = chunk.choices[0]
                if hasattr(choice, 'delta') and hasattr(choice.delta, 'content'):
                    if choice.delta.content is not None:
                        respond.append(choice.delta.content)

        return "".join(respond)

def main():
    st.title(":orange[Olympic Chatbot]")
    st.markdown(':blue[ทดสอบระบบพูดคุยกับ] :violet[Olympic Chatbot] :green[Ai] :red[สุดเหล่ท่อ]:orange[ที่จะตอบคำถามจากงาน โอลิมปิก]')
    st.caption("Powered by Typhoon SCB10x")
    
    with st.sidebar:
        
        a, b, c, d = st.columns(4)
        with b:
            st.image('logo.png', width=125)
                
        st.title("Config")
        st.markdown('Generate key form here https://opentyphoon.ai/')
        
        if "typhoon_api_key" not in st.session_state:
            st.session_state["typhoon_api_key"] = ""
    
        # Input fields
        typhoon_api_key = st.text_input(
            label='TYPHOON API KEY', 
            placeholder='Place key here', 
            value=st.session_state.get('typhoon_api_key', '')
        )
        
        model = st.selectbox(
            label="Model", 
            options=( "typhoon-instruct", "typhoon-v1.5x-70b-instruct"),
            index=st.session_state.get('model_index', 0)
        )
        
        max_token = st.slider(
            label='Max Token', 
            min_value=50, 
            max_value=512, 
            step=10, 
            value=st.session_state.get('max_token', 300)
        )
        
        temperature = st.slider(
            label='Temperature', 
            min_value=0.0, 
            max_value=1.0, 
            step=0.05, 
            value=st.session_state.get('temperature', 0.6)
        )
        
        top_p = st.slider(
            label='Top P', 
            min_value=0.0, 
            max_value=1.0, 
            step=0.05, 
            value=st.session_state.get('top_p', 0.95)
        )

        # Save button
        if st.button('Save Config'):
            st.session_state['typhoon_api_key'] = typhoon_api_key
            st.session_state['model'] = model
            st.session_state['max_token'] = max_token
            st.session_state['temperature'] = temperature
            st.session_state['top_p'] = top_p
            st.success("Configuration saved!")

    with st.chat_message("assistant", avatar='🥐'):
        st.write("สวัสดี มีข้อสงสัยตรงไหนไหมครับ")
                
    prompt = st.chat_input("พิมพ์คำถามตรงนี้!!")
            
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []
        
    if prompt:
        st.session_state['conversation'].append({"role": "user", "content": prompt})

        conversation_history = "\n".join([f"{msg['content']}" for msg in st.session_state['conversation']])
        response = call_llm(st.session_state['typhoon_api_key'], st.session_state['model'], st.session_state['max_token'], st.session_state['temperature'], st.session_state['top_p'], conversation_history)

        st.session_state['conversation'].append({"role": "assistant", "content": response})

        for msg in st.session_state['conversation']:
            with st.chat_message(msg['role']):
                st.write(msg['content'])
                
if __name__ == "__main__":
    main()