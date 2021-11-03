import win32com.client
import os
def merge_presentations(presentations, path):
  ppt_instance = win32com.client.Dispatch('PowerPoint.Application')
  # open the powerpoint presentation headless in background
  prs = ppt_instance.Presentations.open(os.path.abspath(presentations[0]), True, False, False)

  for i in range(1, len(presentations)):
    prs.Slides.InsertFromFile(os.path.abspath(presentations[i]), prs.Slides.Count)

  prs.SaveAs(os.path.abspath(path))
  prs.Close()

path1="E:\myppt.pptx"    
path2="E:\myppt2.pptx"
lst=[path1,path2]
output_path="E:\output.pptx"    # Keep output presentation file path
merge_presentations(lst,output_path)