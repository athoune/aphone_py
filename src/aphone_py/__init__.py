class Phonet(object):

    def __init__(self, desc):
        self.cpt = 0
        for rule in desc['rules']:
            print self.rule(rule)

    def rule(self, rule):
        self.cpt += 1
        txt_size = len(rule['text'])
        if rule['alternates'] != u"":
            txt_size += 1
        fun = """def filter_%i(txt, out):
""" % self.cpt
        #  TODO handles clause as list, and joining with "and"
        #  TODO $ => len == size
        #  TODO handling ^ out == "" ? or a flag?
        if rule['alternates'] != u"":
            fun += """    if len(txt) >= %i and txt[:%i] == u'%s' and txt[%i] in u'%s':
""" % (txt_size, len(rule['text']), rule['text'], len(rule['text']), rule['alternates'])
        else:
            fun += """    if len(txt) >= %i and txt[:%i] == u'%s':
""" % (txt_size, len(rule['text']), rule['text'])

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
