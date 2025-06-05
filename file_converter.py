import markdown
import sys

def convert_markdown():
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    text = ""
        
    with open(input_file, 'r', encoding='utf-8') as f1:
        text = f1.read()
   
    html = markdown.markdown(text,extensions=["tables",'sane_lists'])

    with open(output_file, 'w', encoding='utf-8') as f2:
        f2.write(html)


if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print("入力する引数が足りません")
    command = sys.argv[1]
    if(command == "markdown"):
        convert_markdown()
