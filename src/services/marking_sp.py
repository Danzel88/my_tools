import shutil

import pandas as pd
import docx


class Marking:

    def __init__(self):
        self.data = None

    @staticmethod
    async def copy_file(data):
        """Получаем загруженый файл и копируем его в локальное хранилище
        для обработки
        :return строку с именем файла
        """
        with open(f'{data.filename}', "wb") as buffer:
            shutil.copyfileobj(data.file, buffer)
        return str(data.filename)

    @staticmethod
    async def get_sku_quantity(file_name):
        """Читаем скопированый файл в dataframe из получаем строки с артикулом и
        количеством единиц каждого артикула
        :return dataframe с двумя колонками - артикул и количество
        """
        headers = ["SKU", "Quantity"]
        df = pd.read_excel(file_name, index_col=False, names=headers,
                           header=27, usecols=[3, 27],
                           converters={"SKU": int, "Quantity": int})
        res = df[df["SKU"].apply(lambda x: isinstance(x, int))]
        return res

    async def create_table(self, file) -> dict:
        """
        Преобразуем полученый из get_sku_quantity dataframe в словарь,
        где key это артукул, а value это колчество
        :param file: загруженый из API файл
        :return dict:
        """
        self.data = file
        result = await self.get_sku_quantity(await self.copy_file(self.data))
        dict_result = {}
        for i in result.iterrows():
            dict_result[i[1][0]] = i[1][1]
        await self.create_row(dict_result)
        return result

    async def generate_rows(self, ):
        pass

    async def create_row(self, sku: dict):
        document = docx.Document(r"C:\Users\User\PycharmProjects\my_tools\data\mark_table.docx")
        table = document.tables[0]
        for cell in table.rows[0].cells:
            if not cell.text:
                cell.text = str(sku[30493])
            else:
                cell.text = str(sku[32126])
        document.save('1.docx')



    async def write_in_table(self, sku: dict):
        for k, v in sku.items():
            pass


