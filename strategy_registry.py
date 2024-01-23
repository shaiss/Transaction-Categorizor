class CategorizationStrategy:
  """
  Base class for categorization strategies. All strategies should inherit from this.
  """
  def categorize(self, payee):
      """
      Method to categorize a single payee.
      :param payee: The payee to categorize.
      :return: Categorized payee information.
      """
      raise NotImplementedError

class CategorizationStrategyRegistry:
  """
  Registry for managing categorization strategies.
  """
  _strategies = {}

  @classmethod
  def register_strategy(cls, name, strategy):
      """
      Register a new categorization strategy.
      :param name: Name of the strategy.
      :param strategy: Strategy object.
      """
      cls._strategies[name] = strategy

  @classmethod
  def get_strategy(cls, name):
      """
      Get a categorization strategy by name.
      :param name: Name of the strategy.
      :return: Categorized strategy object.
      """
      return cls._strategies.get(name, None)
