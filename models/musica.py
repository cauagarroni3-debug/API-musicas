from config.conexao import get_connection


class MusicaModel:

    @staticmethod
    def get_all():
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, titulo, artista, album, genero, ano, duracao
            FROM musicas
        """)

        musicas = cursor.fetchall()

        cursor.close()
        conexao.close()

        return musicas


    @staticmethod
    def get_by_id(id):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("""
            SELECT id, titulo, artista, album, genero, ano, duracao
            FROM musicas
            WHERE id = %s
        """, (id,))

        musica = cursor.fetchone()

        cursor.close()
        conexao.close()

        return musica


    @staticmethod
    def criar(titulo, artista, album, genero, ano, duracao):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO musicas
            (titulo, artista, album, genero, ano, duracao)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            titulo,
            artista,
            album,
            genero,
            ano,
            duracao
        )

        cursor.execute(sql, valores)
        conexao.commit()

        id_musica = cursor.lastrowid

        cursor.close()
        conexao.close()

        return id_musica


    @staticmethod
    def deletar(id):
        conexao = get_connection()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM musicas WHERE id = %s",
            (id,)
        )

        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def atualizar(id, titulo, artista, album, genero, ano, duracao):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            UPDATE musicas
            SET titulo = %s,
                artista = %s,
                album = %s,
                genero = %s,
                ano = %s,
                duracao = %s
            WHERE id = %s
        """

        valores = (
            titulo,
            artista,
            album,
            genero,
            ano,
            duracao,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        linhas_afetadas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_afetadas