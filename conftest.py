import schist
import scanpy as sc                          
sc.settings.verbosity=2                           
adata = sc.datasets.blobs() 
sc.tl.pca(adata)                                                        
try:
    sc.pp.neighbors(adata, n_neighbors=3, key_added='foo')
    schist.inference.nested_model(adata, fast_model=True, neighbors_key='foo')          
except TypeError:
    sc.pp.neighbors(adata, n_neighbors=3)
    schist.inference.nested_model(adata, fast_model=True, )

schist.inference.leiden(adata, neighbors_key='foo')
schist.io.write(adata, prefix='test')
adata = schist.io.read(prefix='test')
sc.pp.neighbors(adata, n_neighbors=3)
schist.inference.planted_model(adata, use_weights=False)
schist.inference.planted_model(adata, resume=True, wait=10)
schist.inference.nested_model(adata)
schist.tools.cell_stability(adata)
schist.tools.cluster_consistency(adata, level=2)
