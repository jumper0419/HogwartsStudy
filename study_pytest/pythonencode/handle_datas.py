import yaml

class HandleDatas:
  def get_caculator_datas(name, type="int"):
    with open("../testing/datas/caculator.yml", encoding='utf-8') as f:
      all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]["datas"]
    ids = all_datas[name][type]["ids"]
    return (datas, ids)