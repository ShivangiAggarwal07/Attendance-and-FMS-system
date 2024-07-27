from deepface import DeepFace
objs = DeepFace.analyze(
  img_path = r"C:\Users\harsh\Desktop\Internship\Zigguratss_webapp_Flask\Task 3\face_rec_att_system\images\12313.jpg", 
  actions = ['emotion'],
)
print(objs[0]['dominant_emotion'])