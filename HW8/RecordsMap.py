# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0):
        self.max = max
        self.min = min
        self.pos = (round(pos[0], precision), round(pos[1], precision))

    def add_report(self, temp):
        if temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp

    def __eq__(self, other):
        if other == self.pos:
            return True

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self):
        self._min_buckets = 8
        self.n_buckets = 8
        self.len = 0
        self.L = [[] for i in range(self.n_buckets)]

    def __len__(self):
        return self.len   #returns length of mapping

    def add_report(self, pos, temp):
        lr = LocalRecord(pos, temp, temp)
        index = hash(lr) % self.n_buckets
        if lr in self.L[index]:
            for i in self.L[index]:
                if i == lr:
                    i.add_report(temp)
        elif lr not in self.L[index]:
            self.L[index].append(lr)
            self.len += 1
        if self.len >= 2*self.n_buckets:
            self._rehash(self.n_buckets*2)

    def __getitem__(self, pos):
        lr = LocalRecord(pos)
        index = hash(lr) % self.n_buckets
        if lr in self.L[index]:
            for i in self.L[index]:
                if i == lr:
                    return (i.min, i.max)
        else:
            raise KeyError("Not in Mapping")
  
    def __contains__(self, pos):
        lr = LocalRecord(pos)
        index = hash(lr) % self.n_buckets
        if lr in self.L[index]:
            for i in self.L[index]:
                if i == lr:
                    return True
        else:
            return False

    def _rehash(self, m_new):
        new_bucket = [[] for i in range(m_new)]
        old_buckets = self.L
        self.n_buckets = m_new
        for bucket in old_buckets:
            for item in bucket:
                x = hash(item) % self.n_buckets
                new_bucket[x].append(item)
        self.L = new_bucket
