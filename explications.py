# Par thibaut LOMBARD
import subprocess
from PIL import Image, ImageDraw, ImageFont

def generate_schema_png(filename="hologram_schema.png"):
    width, height = 700, 320
    im = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(im)

    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 128, 0)
    orange = (255, 140, 0)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 11)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 9)
    except:
        font = ImageFont.load_default()
        font_small = font

    rect_size = (400, 300)
    draw.rectangle([0, 0, rect_size[0]-1, rect_size[1]-1], outline=black, width=3)

    draw.line([(rect_size[0]//2, 0), (rect_size[0]//2, rect_size[1])], fill=black, width=2)
    draw.line([(0, rect_size[1]//2), (rect_size[0], rect_size[1]//2)], fill=black, width=2)

    quads = {
        "TL": (0, 0, rect_size[0]//2, rect_size[1]//2),
        "TR": (rect_size[0]//2, 0, rect_size[0], rect_size[1]//2),
        "BL": (0, rect_size[1]//2, rect_size[0]//2, rect_size[1]),
        "BR": (rect_size[0]//2, rect_size[1]//2, rect_size[0], rect_size[1]),
    }

    colors = {
        "TL": red,
        "TR": blue,
        "BL": green,
        "BR": orange,
    }

    padding = 18
    for key, (x0, y0, x1, y1) in quads.items():
        draw.rectangle(
            [x0+padding, y0+padding, x1-padding, y1-padding],
            outline=colors[key],
            width=3
        )

    draw.line(
        [(quads["TL"][0]+padding, quads["TL"][1]+padding), (quads["BR"][2]-padding, quads["BR"][3]-padding)],
        fill=red, width=2)
    draw.line(
        [(quads["TR"][0]+padding, quads["TR"][1]+padding), (quads["BL"][2]-padding, quads["BL"][3]-padding)],
        fill=green, width=2)

    centers = {
        "TL": ((quads["TL"][0] + quads["TL"][2])//2, (quads["TL"][1] + quads["TL"][3])//2),
        "TR": ((quads["TR"][0] + quads["TR"][2])//2, (quads["TR"][1] + quads["TR"][3])//2),
        "BL": ((quads["BL"][0] + quads["BL"][2])//2, (quads["BL"][1] + quads["BL"][3])//2),
        "BR": ((quads["BR"][0] + quads["BR"][2])//2, (quads["BR"][1] + quads["BR"][3])//2),
    }
    for i, key in enumerate(["TL", "TR", "BL", "BR"], 1):
        cx, cy = centers[key]
        draw.text((cx-7, cy-9), str(i), fill=black, font=font)

    legend_x = rect_size[0] + 30
    legend_y = 28
    line_height = 20

    legend_texts = [
        ("1 - Rotation π/4 (45°)", red),
        ("2 - Flip vertical\n+ Rotation π/4", blue),
        ("3 - Flip horizontal\n+ Rotation π/4", green),
        ("4 - Flip horizontal\n+ Rotation 7π/4 (315°)", orange),
    ]

    for text, color in legend_texts:
        draw.multiline_text((legend_x, legend_y), text, fill=color, font=font_small, spacing=3)
        legend_y += line_height * (text.count('\n') + 1)

    im.save(filename)
    print(f"Image PNG générée : {filename}")

latex_template = r"""
\documentclass[a4paper,9pt]{article}
\usepackage{amsmath}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{url}
\geometry{margin=1.2cm}
\pagestyle{empty}

\title{\normalsize\textbf{Transformations géométriques pour la simulation holographique tridimensionnelle}}
\author{\normalsize Thibaut Lombard}
\date{\normalsize 24 juin 2025 \\[8pt]} % un peu plus d'espace

\begin{document}

\maketitle

\small

Ce document décrit un moyen de simuler le rendu holographique 3D à l'aide d'une seule image.
Il s'agit d'appliquer des transformations géométriques qui donnent un effet de perspective grâce à une forme pyramidale.

\vspace{0.3cm}

Soit un point \((x,y)\) dans l'image d'entrée. Les transformations appliquées sont :

\vspace{0.15cm}

\textbf{Rotation} d'un angle \(\theta\) :
\[
R_\theta :
\begin{cases}
x' = x \cos \theta - y \sin \theta \\
y' = x \sin \theta + y \cos \theta
\end{cases}
\]

\vspace{0.15cm}

\textbf{Flip vertical} (axe horizontal) :
\[
F_v :
\begin{cases}
x' = x \\
y' = H - y
\end{cases}
\]

où \(H\) est la hauteur de l'image.

\vspace{0.15cm}

\textbf{Flip horizontal} (axe vertical) :
\[
F_h :
\begin{cases}
x' = W - x \\
y' = y
\end{cases}
\]

où \(W\) est la largeur de l'image.

\vspace{0.3cm}

\textbf{Transformations des quadrants :}

\[
\begin{cases}
T_{TL}(x,y) = R_{\pi/4}(x,y) \\[6pt]
T_{TR}(x,y) = F_v \circ R_{\pi/4}(x,y) \\[6pt]
T_{BL}(x,y) = F_h \circ R_{\pi/4}(x,y) \\[6pt]
\displaystyle
T_{BR}(x,y) = F_h \circ R_{-\pi/4}(x,y)
\end{cases}
\]

\vspace{0.3cm}

\textbf{Explication de la rotation en bas à droite :}

La rotation appliquée au quadrant bas droit est de \(-\pi/4\) (soit \(-45^\circ\)), car elle correspond à une rotation inverse 
par rapport à l'angle de \(\pi/4\) appliqué aux autres quadrants. 

On peut aussi écrire \(-\pi/4\) comme \(7\pi/4\) en notation modulo \(2\pi\) :

\[
7\pi/4 = 2\pi - \pi/4
\]

Cela signifie que la rotation utilisée en bas à droite effectue une rotation de \(315^\circ\) dans le sens horaire, 
équivalente à une rotation de \(-45^\circ\) dans le sens antihoraire.

Ainsi, la transformation \(T_{BR}\) inverse la rotation \(\pi/4\) tout en appliquant un flip horizontal, 
ce qui place correctement l’image dans la pyramide holographique.

\vspace{0.3cm}

Chaque image transformée est positionnée dans une mosaïque \(2 \times 2\) selon le schéma ci-dessous.

\vspace{0.15cm}

\begin{center}
\includegraphics[width=0.78\textwidth]{hologram_schema.png}
\end{center}

\vfill

\footnotesize{
\url{https://github.com/Lombard-Web-Services/HOLO2NET}
}

\end{document}
"""

def generate_pdf(tex_content, filename="transformations_holographie"):
    tex_file = f"{filename}.tex"
    pdf_file = f"{filename}.pdf"

    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(tex_content)

    print("Compilation du document LaTeX...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], check=True)
    print(f"PDF généré : {pdf_file}")

if __name__ == "__main__":
    generate_schema_png()
    generate_pdf(latex_template)
