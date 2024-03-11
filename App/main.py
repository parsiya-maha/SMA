import customtkinter

from welcome_frames import option_frame_text1,option_frame_text2,option_frame_text3
from welcome_frames import more_info_btn,go_to_login

from main_frame import brain_image_label
from main_frame import text1_to_main_frame,text2_to_main_frame,text3_to_main_frame,main_login

from funcs import is_login

from main_upload_image_frame import upload_image_sub_frame



customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk() 
app.after(0, lambda:app.state('zoomed'))
app.title("Mr.Doctor")

frame = customtkinter.CTkFrame(app,width=300)
frame.pack(fill="y",side="left",pady=10)

customtkinter.CTkLabel(frame,
                       width=300,
                       text="Mr.Doctor",
                       font=("...",30,"bold")
                       ).pack(pady=(35,20))

# ------------------------------------------------------------------------------ Option Part and Labels
option_frame = customtkinter.CTkScrollableFrame(frame,height=700)
option_frame.pack(fill="both",padx=10,pady=10)

option_frame_text1(option_frame).pack()
more_info_btn(option_frame).pack()
option_frame_text2(option_frame).pack()
go_to_login(option_frame,app).pack()
option_frame_text3(option_frame).pack()
#github_btn(option_frame).pack()
customtkinter.CTkLabel(option_frame,text="\n\n").pack()


# ----------------------------------------------------------------------------- Main screan

if is_login() :

    main_frame = customtkinter.CTkFrame(app,height=1200)
    main_frame.pack(fill="both",padx=10,pady=10)

    # all main_frame , frames
    main_upload_image_frame = customtkinter.CTkFrame(main_frame,width=800,height=500)
    main_choice_option_frmae = customtkinter.CTkFrame(main_frame,width=370,height=500)
    main_predict_btn_frame = customtkinter.CTkFrame(main_frame,width=800,height=230)
    main_result_frame = customtkinter.CTkFrame(main_frame,width=370,height=230)

    main_upload_image_frame.grid(row=0,column=0,padx=10,pady=10)
    main_choice_option_frmae.grid(row=0,column=1,padx=10,pady=10)
    main_predict_btn_frame.grid(row=1,column=0,padx=10,pady=10)
    main_result_frame.grid(row=1,column=1,padx=10,pady=10)

    # upload image
    upload_image_sub_frame(main_upload_image_frame).pack()



else : 

    main_frame = customtkinter.CTkFrame(app,height=1200)
    main_frame.pack(fill="both",padx=10,pady=10)

    brain_image = brain_image_label(main_frame)
    brain_image.pack(side="right")

    main_text_frame = customtkinter.CTkFrame(main_frame,height=900)
    main_text_frame.pack(fill="both",padx=(80,30),pady=(10,10))

    text1_to_main_frame(main_text_frame).pack()
    text2_to_main_frame(main_text_frame).pack(anchor="w",padx=(105,0))
    main_login(main_text_frame,app).pack(fill="x",padx=(100,105))
    customtkinter.CTkLabel(main_text_frame,text="\n\n\n\n").pack()
    text3_to_main_frame(main_text_frame).pack()



app.mainloop()