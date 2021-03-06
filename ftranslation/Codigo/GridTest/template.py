# -*- coding: utf-8 -*-


from randomHCNFTest import RandomHCNFTest


#from htab        import HTab
#from hyloresv2_3 import HyLoResV2_3
from spass import SPASS
from htab import HTab
from eprover import E
from functionalTranslation import FunctionalTranslation
from optimizedFunctionalTranslation import OptimizedFunctionalTranslation



def configureTest():
  test  = RandomHCNFTest(testId         = 'rereflexive',
                         # Number of atoms
                         numOfProps     = 3, freqOfProps = 1,
                         numOfNoms      = 0, freqOfNoms  = 0,
                         numOfSVars     = 0, freqOfSVars = 0,
                         # Number and depth of modalities
                         numOfRels      = 1, maxDepth    = 3,
                         diamDepth      = 3, freqOfDiam  = 1,
                         atDepth        = 0, freqOfAt    = 0,
                         downDepth      = 0, freqOfDown  = 0,
                         invDepth       = 0, freqOfInv   = 0,
                         univDepth      = 0, freqOfUniv  = 0,
                         diffDepth      = 0, freqOfDiff  = 0,
                         # Test structure
                         batchSize      = 50,
                         fromNumClauses = 41,
                         toNumClauses   = 241,
                         step           = 20,
                         timeout        = 30,
                        )

  test.dirStructure.setNewScratchDirFor(test.testId)
  test.setProvers(proverConfiguration(test.dirStructure))
 
  return test


def proverConfiguration(dirStructure):
  binpath = dirStructure.binDir
  
  cabal_path = '~/.cabal/bin/'

  withSorts_spass = FunctionalTranslation('ftrans', cabal_path, 'withSorts-spass')
  withSortsAllIn_spass = FunctionalTranslation('ftrans', cabal_path, 'withSortsAllIn-spass')
  withSortsAllOut_spass = FunctionalTranslation('ftrans', cabal_path, 'withSortsAllOut-spass')

  withoutSorts_spass = OptimizedFunctionalTranslation('oftrans', cabal_path, 'withoutSorts-spass')
  fthl_spass = FunctionalTranslation('ftrans', cabal_path, 'fthl-spass')
  pnffthl_spass = OptimizedFunctionalTranslation('oftrans', cabal_path, 'pnffthl-spass')
  ufthl_spass = OptimizedFunctionalTranslation('oftrans', cabal_path, 'ufthl-spass')
  eager_spass = OptimizedFunctionalTranslation('oftrans', cabal_path, 'eagerSortsRemTrans-spass')
  modalSpass = OptimizedFunctionalTranslation('oftrans', cabal_path, 'modal-spass')
  modalSpass2 = OptimizedFunctionalTranslation('oftrans', cabal_path, 'modal-spass2')
  
  gridTestBinPath = "/home/mdiaz1/repo/ftranslation/Codigo/GridTest/bin"	
	
  allOut_spass = SPASS('allOut_spass',  gridTestBinPath, 'SPASS', translation=withSortsAllIn_spass)
  funcTrans_spass = SPASS('fun_spass',  gridTestBinPath, 'SPASS', translation=fthl_spass, options="-CNFOptSkolem=0")
  funcTrans_spass2 = SPASS('fun_spass_sorts0', gridTestBinPath, 'SPASS', translation=ufthl_spass)		
  optimised_spass = SPASS('opt_spass',  gridTestBinPath, 'SPASS', translation=withSorts_spass, options="-CNFOptSkolem=0")
  withoutSorts_spass = SPASS('opt_sin_sorts_spass',   gridTestBinPath, 'SPASS', translation=withoutSorts_spass, options="-CNFOptSkolem=0")
  withoutSortsNoPNF_spass = SPASS('fun_sin_sorts_spass',   gridTestBinPath, 'SPASS', translation=eager_spass, options="-CNFOptSkolem=0")
  withoutSortsNoPNF_spass2 = SPASS('fun_sin_sorts_spass_sorts0', gridTestBinPath, 'SPASS', translation=eager_spass, options="-Sorts=0")		

  pnfFuncTrans_spass = SPASS('pnfFuncTrans_spass',   gridTestBinPath, 'SPASS', translation=pnffthl_spass)

  std_mspass = SPASS('std_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass, options="-EMLTranslation=0")
  fun_mspass = SPASS('fun_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass,  options="-EMLTranslation=1")
  opt_mspass = SPASS('opt_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass,  options="-EMLTranslation=2")
  semi_fun_mspass = SPASS('semi_fun_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass , options="-EMLTranslation=3")
  tree_layered_mspass = SPASS('tree_layered_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass , options="-EMLTranslation=0 -EMLFuncNary=1")

  pol_fun_mspass = SPASS('pol_fun_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass,  options="-EMLTranslation=1 -EMLFuncNary=1")
  pol_opt_mspass = SPASS('pol_opt_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass,  options="-EMLTranslation=2 -EMLFuncNary=1")

  rel_rel_mspass = SPASS('rel_rel_mspass',   gridTestBinPath, 'SPASS', translation=modalSpass,  options="-EML2Rel=1")


  funcTrans_tptp = OptimizedFunctionalTranslation('funcTrans-tptp', cabal_path, 'funcTrans-tptp')
  pnfFuncTrans_tptp = OptimizedFunctionalTranslation('pnfFuncTrans-tptp', cabal_path, 'pnfFuncTrans-tptp')
  withSorts_tptp = OptimizedFunctionalTranslation('withSorts-tptp', cabal_path, 'withSorts-tptp')
  withoutSorts_tptp = OptimizedFunctionalTranslation('withoutSorts-tptp', cabal_path, 'withoutSorts-tptp')
  eager_tptp = OptimizedFunctionalTranslation('eager-tptp', cabal_path, 'eagerSortsRemTrans-tptp')

  htab1 = HTab('htab', binpath, 'htab')

  funcTrans_eprover = E('funcTrans_eprover', binpath, 'tptp3', translation=funcTrans_tptp)
  pnfFuncTrans_eprover = E('pnfFuncTrans_eprover', binpath, 'tptp3', translation=pnfFuncTrans_tptp)
  optimised_eprover = E('optimised_eprover', binpath, 'tptp3', translation=withSorts_tptp)
  withoutSorts_eprover = E('withoutSorts_eprover', binpath, 'tptp3', translation=withoutSorts_tptp)
  withoutSortsNoPNF_eprover = E('withoutSortsNoPNF_eprover', binpath, 'tptp3', translation=eager_tptp)

#  return [withoutSorts_spass]
#  return [withoutSortsNoPNF_spass]
#  return [semi_fun_mspass]						
#  return [htab1, funcTrans_spass, optimised_spass, allOut_spass]
#  return [funcTrans_spass]
#  return [htab1]
#  return [htab1, funcTrans_spass, withoutSortsNoPNF_spass]
  return [htab1, funcTrans_spass, withoutSortsNoPNF_spass, optimised_spass, withoutSorts_spass]
#  return  [htab1, funcTrans_eprover, optimised_eprover, withoutSorts_eprover, withoutSortsNoPNF_eprover]
