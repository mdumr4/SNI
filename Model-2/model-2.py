from ultralytics import YOLO

# model = YOLO("yolo12n.pt")

# results = model.train(
#   data='./Data/data.yaml',
#   epochs=30,
#   batch=4,
#   imgsz=320,
#   scale=0.5,  # S:0.9; M:0.9; L:0.9; X:0.9
#   mosaic=0.7,
#   mixup=0.0,  # S:0.05; M:0.15; L:0.15; X:0.2
#   copy_paste=0.05,  # S:0.15; M:0.4; L:0.5; X:0.6
#   device="cpu",
# )


model = YOLO("runs/detect/train/weights/best.pt")
results = model.predict(
    source="Data/test/images",
    conf=0.25,
    save=True,
    save_txt=True,
    save_conf=True,
    show=True,
    device="cpu",
)