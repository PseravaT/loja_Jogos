from config.bd import criar_conexao

def listagem():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT titulo, subtitulo From lojogos.jogos ORDER BY titulo ASC;"
        cursor.execute(query,())
        conn.commit()
        resultado = cursor.fetchall()
        for titulo, subtitulo in resultado:
             print(f" {titulo}: {subtitulo}")

        
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()

def buscaLetra(letra):
    conn = criar_conexao()

    try:
        cursor = conn.cursor() 
        query = "SELECT titulo, subtitulo FROM lojogos.jogos WHERE titulo LIKE %s OR subtitulo LIKE %s ORDER BY titulo DESC;"
        cursor.execute(query, (f'{letra}%', f'{letra}%'))
        conn.commit()
        resultado = cursor.fetchall()
        if resultado:
            for titulo, subtitulo in resultado:
                 print(f"jogos: {titulo}: {subtitulo}")
        else:
            print("Nenhum jogo encontrado com a letra especificada.")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        
 