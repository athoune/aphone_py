from cStringIO import StringIO


class Phonet(object):

    def __init__(self, desc, target=StringIO()):
        self.cpt = 0
        filters = {}
        for key, rules in desc['rules'].items():
            for rule in rules:
                self.cpt += 1
                target.write(self.rule(rule).encode('utf-8'))
                if key not in filters:
                    filters[key] = []
                filters[key].append("filter_%i" % self.cpt)
        print filters
        print target.getvalue()

    def rule(self, rule):
        txt_size = len(rule['text'])
        if rule['alternates'] != u"":
            txt_size += 1
        fun = """# %s
def filter_%i(txt, out):
    if """ % (rule['raw'], self.cpt)
        #  TODO handling ^ out == "" ? or a flag?
        filters = []
        if rule['ending']:
            filters.append("len(txt) >= %i" % txt_size)
        else:
            filters.append("len(txt) == %i" % txt_size)
        filters.append("txt[:%i] == u'%s'" % (len(rule['text']), rule['text']))
        if rule['alternates'] != u"":
            filters.append("txt[%i] in u'%s'" % (len(rule['text']), rule['alternates']))
        fun += " and ".join(filters)
        fun += ":\n"

        if rule['replace'] == u"_":
            replace = u""
        else:
            replace = rule['replace']
        if rule['again']:
            fun += """        return u"%s" + txt[%i:], out
""" % (replace, len(rule['text']) - rule['minus'])
        else:
            fun += """        return txt[%i:], out += u"%s"
""" % (len(rule['text']) - rule['minus'], replace)
        return fun


class Filter(object):
    rules = {}

    def filter(self, txt):
        upper = txt.decode('utf-8').upper().encode('utf-8')
        encoded = u""
        while upper != u"":
            letter = upper[0]
            if letter not in self.rules:
                upper = upper[1:]
                encoded += letter
            else:
                upper, encoded = self.rules[letter].filter(upper)
        return encoded
