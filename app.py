from fastai.vision.all import *
import gradio as gr

#load a pickle file which containes the trained model
learn = load_learner('trained_models/export.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    # the prediciton of the image from the trained model
    pred,pred_idx,probs = learn.predict(img)
    #return the probability that the breed of the image is correct
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

#launch the trained model in a Gradio web app
gr.Interface(fn=predict, inputs=gr.Image(width=512, height=512), outputs=gr.Label(num_top_classes=5)).launch(share=True)

