from ultralytics import YOLO
import cv2 as cv
import logging

logging.getLogger('ultralytics').setLevel(logging.WARNING)

class Jacket_detection():
    def __init__(self, jacket_path, people_path):
        self._people_model = YOLO(people_path)
        self._jacket_model = YOLO(jacket_path)

    def find_centers(self, boxes):
        centers = []
        for box in boxes:
            x1, y1, x2, y2 = box
            center = [(x1+x2)/2, (y1+y2)/2]
            centers.append(center)
        return centers

    def predict_video(self, filename):

        cap = cv.VideoCapture(filename)

        fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Используйте кодек X264 для записи в MP4
        fps = 24.0  # Фреймрейт

        first = True
        while True:
            # Читаем кадр из веб-камеры
            ret, frame = cap.read()

            if first:
                shape = frame.shape
                frame_size = (shape[1], shape[0])  # Размер кадра
                out = cv.VideoWriter('output.mp4', fourcc, fps, frame_size)

                first = False

            if not ret:
                break

            frame = model.predict_image(frame)
            out.write(frame)
            # Отображаем кадр
            cv.imshow('Video', frame)
            # Если нажата клавиша 'q' - выходим из цикла
            if cv.waitKey(1) & 0xFF == ord('q'):
                break


    def predict_image(self, img):
        
        people_results = self._people_model(img)
        jacket_results = self._jacket_model(img)

        people_boxes = [box.xyxy[0].tolist() for box in people_results[0].boxes if box.conf > 0.8]
        jacket_boxes = [box.xyxy[0].tolist() for box in jacket_results[0].boxes if box.cls == 1]
        
        jacket_centres = self.find_centers(jacket_boxes)

        people_results[0].save(filename='people.jpg')
        jacket_results[0].save(filename='jacket.jpg')
        #print(people_boxes)
        #print(jacket_boxes)
        violation = False
        for person in people_boxes:
            #print(person)
            jacket_in = False
            for jacket in jacket_centres:
                if person[0] <= jacket[0] <= person[2] and person[1] <= jacket[1] <= person[3]:
                    jacket_in = True

            if not jacket_in:
                cv.rectangle(img, (int(person[0]), int(person[1])), (int(person[2]), int(person[3])), (0, 0, 255), 2)
                violation = True
                #print("НАРУШЕНИЕ!!!!")
    

        #cv.imwrite('result.png', img)
        return (img, violation)

if __name__ == "__main__":
    model = Jacket_detection()
    image = cv.imread('./test_images/test2.jpeg')

    model.predict(image)