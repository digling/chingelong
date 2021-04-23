from lingpy.compare.partial import Partial
from lingpy.align.sca import Alignments
from lexibank_chingelong import Dataset

# Load data
#part = Partial.from_cldf('cldf/cldf-metadata.json')
part = Partial.from_cldf(Dataset().cldf_dir.joinpath('cldf-metadata.json'))

# Compute cognate sets according to SCA (appended to the column cogids)
part.partial_cluster(threshold=0.45, ref="cogids", cluster_method="upgma")

# Compute cognate sets according to LexStat (appended to the column lexstatids)
part.get_partial_scorer(runs=1000)
part.partial_cluster(method='lexstat', threshold=0.55, cluster_method='upgma', ref="lexstatids")

# Align the partial cognates
alms = Alignments(part, ref='cogids')
alms.align()

# Write the data to a file
alms.output('tsv', filename='alignments', ignore='all', prettify=False)

