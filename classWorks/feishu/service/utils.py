import yaml


class Utils:
  @classmethod
  def load_yaml(cls, path, type=""):
    """
    将yaml文件流转成json对象
    :param path: yaml文件的路径
    :param type: 数据类型，默认为空
    :return: json_object
    """
    datas = []
    if path != "":
      with open (path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
      if type == "":
        return datas
      else:
        return datas[type]
    return datas