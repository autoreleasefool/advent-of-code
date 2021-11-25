from enum import Enum
from os import path


class Language(Enum):
  HASKELL = 'haskell'
  PYTHON = 'python'
  RUBY = 'ruby'
  RUST = 'rust'
  SWIFT = 'swift'

  @property
  def file_extension(self):
    match self:
      case Language.HASKELL: return '.hs'
      case Language.PYTHON: return '.py'
      case Language.RUBY: return '.rb'
      case Language.RUST: return '.rs'
      case Language.SWIFT: return '.swift'

  @property
  def compiled_extension(self):
    match self:
      case Language.HASKELL: return '.hsx'
      case Language.PYTHON: return None
      case Language.RUBY: return None
      case Language.RUST: return None
      case Language.SWIFT: return '.o'

  @property
  def compilation_command(self):
    match self:
      case Language.HASKELL: return ['stack', 'ghc', '--']
      case Language.PYTHON: return None
      case Language.RUBY: return None
      case Language.RUST: return None
      case Language.SWIFT: return ['swiftc']

  @property
  def src_prefix(self):
    match self:
      case Language.HASKELL: return None
      case Language.PYTHON: return None
      case Language.RUBY: return None
      case Language.RUST: return 'src'
      case Language.SWIFT: return None

  @property
  def compile_from_directory(self):
    match self:
      case Language.HASKELL: return False
      case Language.PYTHON: return False
      case Language.RUBY: return False
      case Language.RUST: return True
      case Language.SWIFT: return True

  @property
  def starter_file(self):
    return path.join('.', 'util', self.value, f'starter{self.file_extension}')

  @property
  def supporting_files_directory(self):
    return path.join('.', 'util', self.value, 'supporting_files')
