import sqlite3,os
import pygame
from classes.constants import WIDTH, BLACK, WHITE
from functions import *


def create_scores_table():
    """
    Se encarga de crear una tabla llamada "scores" en la base de datos. 
    Verifica si la tabla ya existe, y si no es así, la crea con dos columnas: 
    "name" (texto) y "score" (entero). 
    Utiliza la biblioteca sqlite3 para conectarse a la base de datos y 
    ejecutar la consulta necesaria.
    """

    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    db_path = os.path.join(script_dir, "scores.db") 
    
    conn = sqlite3.connect(db_path) 
    
    c = conn.cursor() 
    
    c.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")
    # Ejecuta una consulta SQL para crear una tabla llamada "scores" con una columna llamada "score" de tipo INTEGER, si no existe previamente.
    conn.commit() # Confirma los cambios realizados en la base de datos.
    conn.close() # Cierra la conexión a la base de datos.

def save_score(name, score):
    """
    Guarda un puntaje en la base de datos. Recibe como parámetros el nombre y el puntaje a guardar. 
    Primero, se conecta a la base de datos y obtiene el puntaje más alto existente. 
    Si el puntaje pasado como parámetro es mayor que el puntaje más alto existente o no hay puntaje 
    existente, se elimina el puntaje existente (si hay alguno) y se inserta el nuevo puntaje en 
    la tabla "scores". La función asegura que el puntaje se almacene como un número entero.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")

    # Conectar a la base de datos y obtener los 10 mejores puntajes actuales
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 10")
    current_scores = c.fetchall()

    if len(current_scores) < 10 or score > current_scores[-1][0]:
        # Eliminar el puntaje más bajo si la tabla está llena
        if len(current_scores) >= 10:
            lowest_score = current_scores[-1][0]
            c.execute("DELETE FROM scores WHERE score=?", (lowest_score,))

        # Insertar el nuevo puntaje en la tabla
        c.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, int(score)))

    conn.commit()
    conn.close()

def show_scores():
    """
    Su objetivo es mostrar los puntajes almacenados en una base de datos SQLite en 
    una interfaz gráfica utilizando la biblioteca Pygame.
    """
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consulta SELECT para obtener los puntajes
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
    scores_list = cursor.fetchall()

    conn.close()

    screen.fill(BLACK)  # Limpia la pantalla
    font = pygame.font.SysFont('Calibri', 20)
    y = 100  # Posición vertical inicial para mostrar los puntajes

    # Encabezado de la tabla
    header_text = font.render("Top 10 Scores", True, WHITE)
    header_rect = header_text.get_rect(center=(WIDTH // 2, y))
    screen.blit(header_text, header_rect)
    y += 50

    # Mostrar los puntajes en la tabla
    for i, score in enumerate(scores_list, start=1):
        score_text = font.render(f"{i}. {score[0]} - {score[1]}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, y))
        screen.blit(score_text, score_rect)
        y += 40

    pygame.display.flip()  # Actualiza la pantalla    

def check_if_table_exists():
    """
    Verifica si la tabla "scores" existe en la base de datos. 
    Utiliza una consulta para buscar la tabla en el esquema de la base de datos. 
    Devuelve True si la tabla existe y False en caso contrario.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verificar si la tabla "scores" existe en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scores'")
    table_exists = cursor.fetchone() is not None

    cursor.close()
    conn.close()

    return table_exists

def get_highest_score():
    """
    Obtiene el puntaje más alto registrado en la tabla "scores". 
    Se conecta a la base de datos, ejecuta una consulta que devuelve el máximo puntaje de la columna 
    "score" y luego extrae el valor del resultado obtenido. Si no hay puntajes registrados, devuelve 0.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtener el puntaje más alto de la tabla "scores"
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()
    highest_score = result[0] if result and result[0] else 0

    cursor.close()
    conn.close()

    return highest_score

def get_highscore_name():
    """
    Obtiene el nombre asociado al puntaje más alto registrado en la tabla "scores". 
    Primero, obtiene el puntaje más alto utilizando la función get_highest_score(). 
    Luego, ejecuta una consulta para obtener el nombre correspondiente a ese puntaje. 
    Si se encuentra un resultado, se extrae el nombre; de lo contrario, se devuelve "N/A" (no disponible).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtener el puntaje más alto de la tabla "scores"
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()
    highest_score = result[0] if result and result[0] else 0

    # Obtener el nombre asociado al puntaje más alto
    cursor.execute("SELECT name FROM scores WHERE score=?", (highest_score,))
    result = cursor.fetchone()
    highest_score_name = result[0] if result else "N/A"

    cursor.close()
    conn.close()

    return highest_score_name
