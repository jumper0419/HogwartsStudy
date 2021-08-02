import yaml


class Utils:
  @classmethod
  def yaml_load(self, path, key_words=""):
    datas = []
    if path != "":
      with open(path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
      if key_words == "":
        return datas
      else:
        return datas[key_words]
    return datas